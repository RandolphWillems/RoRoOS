#!/usr/bin/env python3
import hashlib
import json
import os
import shutil
import sys
import urllib.request
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            digest.update(chunk)
    return digest.hexdigest()


def download_file(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f'Downloading {url} to {dest}')
    with urllib.request.urlopen(url) as response, dest.open('wb') as out:
        shutil.copyfileobj(response, out)


def main(manifest_path: str) -> int:
    manifest_file = Path(manifest_path)
    if not manifest_file.is_file():
        print(f'Manifest not found: {manifest_file}', file=sys.stderr)
        return 3

    with manifest_file.open('r', encoding='utf-8') as f:
        manifest = json.load(f)

    base_dir = manifest_file.parent.parent.resolve()
    packages_dir = base_dir / 'packages'
    packages_dir.mkdir(parents=True, exist_ok=True)

    print(f'Loaded manifest: {manifest_file.name}')
    print(f'Update name: {manifest.get("name", "Unnamed")}, version: {manifest.get("version", "n/a")}')

    if manifest.get('signed'):
        print('WARNING: signed update manifests are not yet verified by this script.')

    packages = manifest.get('packages', [])
    if not packages:
        print('No packages found in manifest.', file=sys.stderr)
        return 4

    for pkg in packages:
        path = pkg.get('path')
        filename = pkg.get('filename') or Path(path).name
        url = pkg.get('url')
        checksum = pkg.get('sha256', '')

        if not path and not url:
            print('Package entry must include path or url.', file=sys.stderr)
            return 5

        local_package = packages_dir / filename

        if url and not local_package.exists():
            download_file(url, local_package)
        elif Path(path).is_file():
            src = Path(path).resolve()
            if src != local_package:
                print(f'Copying local package {src} to {local_package}')
                shutil.copy2(src, local_package)
        elif local_package.exists():
            print(f'Using existing package: {local_package}')
        else:
            print(f'Package not found: {path}', file=sys.stderr)
            return 6

        if checksum:
            actual = sha256_file(local_package)
            if actual.lower() != checksum.lower():
                print(f'Checksum mismatch for {filename}: expected {checksum}, got {actual}', file=sys.stderr)
                return 7
            print(f'Checksum verified for {filename}')
        else:
            print(f'No checksum provided for {filename}, skipping verification.')

    print('Update manifest processed successfully.')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <manifest.json>', file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
