# Changelog

## 0.8.0 (2026-05-06)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([1c10c88](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/1c10c88c91449891a7cd8a5e6e937f8b2bb8ab3e))
* **api:** api update ([66f3bd8](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/66f3bd8f632c1258d8013c87b0cb332289c61a29))

## 0.7.0 (2026-05-01)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([1c64ccd](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/1c64ccd6cc2d84638873959dd60b4556b0824d38))


### Chores

* **internal:** reformat pyproject.toml ([15650b5](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/15650b5ff32df5dee3c4789b7fb5f695b0a1e7ed))

## 0.6.0 (2026-04-30)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.5.0...v0.6.0)

### Features

* support setting headers via env ([7092850](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/7092850e1a84d2161f9df2c95f02511bdf69a099))


### Bug Fixes

* use correct field name format for multipart file arrays ([d6aae9f](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/d6aae9f9f2b6fe2c281c61404abd93142b4c6247))

## 0.5.0 (2026-04-27)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([5af1596](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/5af1596261d34518d88d1ca639a1927476af82cc))
* **api:** api update ([80e68ca](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/80e68cae8da723b0bfe02f8a211d817ea90571c2))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([02e07ed](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/02e07ed1709b0b89fc0b00e4a0e49d35fd21bf87))


### Chores

* **internal:** more robust bootstrap script ([311789c](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/311789cd617535751d9f2fe0eb6fec2847182ebd))

## 0.4.0 (2026-04-11)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([a5fc6c1](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/a5fc6c1782e755642692cbf223e18418948df2d1))
* **internal:** implement indices array format for query and form serialization ([ff6cfc3](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/ff6cfc38b19d0ffdf9856b7f3a0c11dfb6914657))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([cc5a8f4](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/cc5a8f46c018b8c795d790a277c3b97a66c0acff))
* ensure file data are only sent as 1 parameter ([64052ee](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/64052ee5ffa70fbfc5dd567db2ea4b16584842c3))


### Chores

* **ci:** skip lint on metadata-only changes ([c4bec15](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/c4bec15a116ae383b938c7dffafeaea557e1a3fb))
* **internal:** update gitignore ([fa608cc](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/fa608ccb0f761aca80fb97c51a50b2d69233f285))


### Documentation

* improve examples ([bcfe13b](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/bcfe13b38a9e638a1ceed8404c1815ef2a036e87))

## 0.3.0 (2026-03-20)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([69b21d3](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/69b21d37b5ad5a92f0004c29b33deabbd2d96191))


### Bug Fixes

* sanitize endpoint path params ([5df3952](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/5df3952a4e3b533023374c83bdc6a07db13d43a8))

## 0.2.0 (2026-03-18)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** api update ([438a91a](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/438a91a5e8f50bd4a38b6feb259dad63d5d440f6))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([9527c40](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/9527c4029bb2fadf5317f1a72fc3c79f39367f8a))
* **pydantic:** do not pass `by_alias` unless set ([52dbac9](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/52dbac91a77497a3f205fca239b8ed9c43954f08))


### Chores

* **internal:** tweak CI branches ([a044472](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/a0444720e67449ae6ed83d4d96f1cd6f32ed64ae))

## 0.1.0 (2026-03-12)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/AlphaxivCat/alphaxiv_cat-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([780ee59](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/780ee59bb3c4d2e926b9d90beb0d926aeff183b7))


### Chores

* update SDK settings ([cc961f6](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/cc961f6b7ce42476ef2eac1db99e21a76f30c2da))
* update SDK settings ([74004da](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/74004da415d4d8b1f68d9bc160d5d16a47053cf5))
* update SDK settings ([d695929](https://github.com/AlphaxivCat/alphaxiv_cat-python/commit/d69592934352b7b25fcf7fe8fd4de41690b85e53))
