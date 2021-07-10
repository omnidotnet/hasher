# Hasher
*If you need a hash, we've got your back.*
## What's Hasher?
Hasher is an **open-source** and **free to use** software. The aim of Hasher is to provide an easy way to make random hashes, that doesn't imply the download of some crypto-mining program that logs hashes and nonces and more nonsense. 
Hasher is designed to just give you hashes - as easy as that.

## What can Hasher do?
If I were to explain you in the simplest (and probably most accurate) way, it just gives you 10 hashes. I will enter into detail later.

### What should I use Hasher for?
Hasher can be used for almost anything, so I will list examples of what Hasher does and doesn't.

- Hasher **is**:
	- A random value generator
	- A sha256 system test
	- A roleplaying tool
- Hasher **isn't**:
	- A password generator
	- A ransomware decryptor
	- A cryptocurrency miner

## How does Hasher work?
Hasher takes 10 random numbers from *0* to *999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999*, and then encodes them to a string that Python's "hashlib" can understand. Hasher then takes the sha256 hash, re-encodes it, and passes it through another sha256 algorithm.

## What can I do with Hasher's source code?
Hasher uses the GNU-GPLv3 license, which essentially means that you can do anything with my code except making it closed-source.
