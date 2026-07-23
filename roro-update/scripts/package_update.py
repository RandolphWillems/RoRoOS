#!/usr/bin/env python3
import argparse
import hashlib
import json
import tarfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    import hashlib
    digest = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            digest.update(chunk)
    return digest.hexdigest()


def make_package(source: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(dest, 'w:gz') as tar:
        tar.add(source, arcname=source.name)


def main():
    parser = argparse.ArgumentParser(description='Package update bundle and generate manifest')
    parser.add_argument('source', type=Path, help='Path to source folder to package')
    parser.add_argument('--version', required=True, help='Update version')
    parser.add_argument('--release-notes', default='', help='Release notes')
    parser.add_argument('--output', type=Path, default=Path('packages'), help='Output folder for package')
    parser.add_argument('--name', default='RoRoOS Base', help='Update display name')
    args = parser.parse_args()

    if not args.source.exists():
        raise SystemExit(f'Source path not found: {args.source}')

    package_name = f'{args.source.name}-{args.version}.tar.gz'
    package_path = args.output / package_name
    make_package(args.source, package_path)

    manifest = {
        'name': args.name,
        'version': args.version,
        'releaseNotes': args.release_notes,
        'packages': [
            {
                'name': args.source.name,
                'path': str(package_path.relative_to(Path.cwd())),
                'filename': package_name,
                'url': str(package_path.relative_to(Path.cwd())),
                'sha256': sha256_file(package_path),
                'size': package_path.stat().st_size,
                'notes': f'Package for {args.source.name} update',
            }
        ],
        'signed': False,
        'signature': '',
    }

    manifest_path = args.output.parent / 'manifests' / 'update-manifest.json'
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open('w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    print(f'Created package: {package_path}')
    print(f'Created manifest: {manifest_path}')


if __name__ == '__main__':
    main()
