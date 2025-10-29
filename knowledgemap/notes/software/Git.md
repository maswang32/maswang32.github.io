# Git 

Source:

https://tom.preston-werner.com/2009/05/19/the-git-parable.html

- To summarize the first few sections, imagine saving snapshots of your code in branches. Branches cannot have branches.
- each branch is identified by the latest snapshot on that branch. This makes it easy to trace back the lineage of snapshots on the branch.
- the name of each branch is associated with the latest snapshot on each branch.
- We can also have pointers to snapshots that refer to a single snapsnot, without moving. These are tags.


- Snapshots are named by the commit message, which actually includes the author name, email, date, and parent snapshot. This information is hashed.

- snapshots can be created and moved around between computers without losing their identity or location in the tree - they are still identified by a SHA1 hash. They can be private, too.


## Merging
- merging two snapshots into one - you have two parents now.
- the merge snapshot only contains the changes necessary to merge.
- you fetch all of your collaborator's snapshots, and dthey fetch yours.

## Rewriting history
- you can do this too, make new snapshot and point it to an old one, then have the branch be associated with your new snapshot. this cuts off some snapshots, but you can delete them.

## Staging
- staging is basically saying which files we are going to put in a snapshot.

## Diffs
- you can also see diffs between working directory and staged, and staged and snapshot.

## Deduping
- long explanation

Last Reviewed: 6/20/25