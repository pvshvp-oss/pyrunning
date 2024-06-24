# Contributing

## Release Checklist

- [ ] Build and test the package locally: `sh packaging/setup.sh local`

- [ ] Update the version and changelog in [CHANGELOG.md](CHANGELOG.md)

- [ ] Update the version in 
  - [ ] [The PKGBUILD for the stable variant of the package](packaging/python-pyrunning/PKGBUILD)
  - [ ] [The PKGBUILD for the git variant of the package](packaging/python-pyrunning-git/PKGBUILD)
  - [ ] [The PKGBUILD for the local variant of the package](packaging/python-pyrunning-local/PKGBUILD)

- [ ] Commit and push all changes through git, for example `git commit -m "Some message" && git push`

- [ ] Create and push a tag, for example `git tag -s -a v0.0.15 -m "This is version 0.0.15" && git push origin v0.0.15`
- [ ] If there was a mistake and if you want to yank the release, run something like `git tag -d v0.0.15 && git push --delete origin v0.0.15`. Then the errors can be fixed and the previous step can be repeated to create a new tag.