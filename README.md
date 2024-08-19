# Hasher
*If you need a hash, we've got your back.*
## What's Hasher?
Hasher is FOSS, and will always be so. The aim of Hasher is to provide an easy way to make random hashes, for whatever you want them. No crypto or anything, just ten hash strings. 

## What can Hasher do?
The short answer is that it gives you 10 random hashes of an algorithm of your choice, that you can choose to save to a .txt file. The long answer is basically the rest of the readme.

### What should I use Hasher for?
Hashes can be used for lots of things, and so can Hasher. Here's a short list of what Hasher is and isn't.

- Hasher **is**:
	- A random value generator
	- A sha256/sha512/sha1/md5 system test
	- A roleplaying tool (for whatever RP you need hashes, I guess)
- Hasher **isn't**:
	- A password generator
	- A ransomware decryptor
	- A cryptocurrency miner

## How does Hasher work?
Hasher takes 10 random numbers from *0* to *999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999*, and then encodes them into a string that Python's "hashlib" can understand. Hasher then takes the hash, re-encodes it, and passes it through another instance of the same algorithm. You can read the code for a more in-depth explanation.

### What algorithms can I use?
At the moment, we've got 4 algorithms! Type:
- "md5" for MD5.
- "sha1" for SHA1.
- "sha256" for SHA256
- "sha512" for SHA512.

## What can I do with Hasher's source code?
Hasher uses the GNU-GPLv3 license, which essentially means that you can do anything with my code except making it closed-source.

## How do I install Hasher?
Download the latest .py file, make sure you have Python installed, and run it. It's a CLI tool, but it's pretty simple, all you need to do is input your preferred algorithm and get your hashes.
