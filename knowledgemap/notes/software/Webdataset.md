# Webdataset

- .tar files store things in continuous chunks
- HDP for distributed storage protocol - use any webserver.
- works for local files.
- implements IterableDataset
- all datasets are POSIX tar archives
    - create using tar, or the tar writer class in the library
    - all I/O is sequential.
- refer to webdatasets by using a filepattern.
- consists of many shards.
- url = ...
- dataset = wds.Dataset(url) 
- you might want to do decompression
- iterating:
    - key is the file extension
    - value = binary content
    - __key__ is the sample itself, common basename that is for the sample.
    - decodings are standard. use .decode() to turn into dictionary of all files comprised in a sample, which can be turned into a tuple, then apply transforms.
    - Then you can shuffle.
    dataset = (
        wds.Dataset(url, length=10000)
        .decode("pil")
        .to_tuple("ppm", "cls")
        .shuffle(10000)
    )

## Creating a Webdataset:
- .tar file
- files with a common basename make up a sample.
- basename = same samples
- speaker1/sample1.txt
- speaker1/sample1.wav  
- can just make a tar archive.
- basename is ALL extensions removeL sample.input.png -> sample
    - the key is 'sample', the dictionary entries are input.png/ 
- use tar
- for labels can look up metadata.

## avoiding extra storage
- instead of storing a ton of files,
- create a recipe then use "tarp create"
- filename/source table. 


## ShardWriter
- ensures each file is less than a certain size and has less than a given number of samples.


## More practical stuff
- Use resample = True, which will mean that if a worker runs out of data on their shard, they
simply find ("sample") a new shard
- batch in the webdataset
- see fmdiffae code
Last Reviewed: 5/1/25