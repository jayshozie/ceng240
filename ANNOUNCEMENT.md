# What happened?

The book is copyrighted, had to remove the book from the repository. Deleting
a file from a repository does not remove it from the history. The book was
still accessible in the history, thus complete removal of the repository.

# Couldn't you just change the history of the repository?

Yeah, about that. Please check 'How did you manage to delete the files?'
section lol.

# What is going to happen?

Hopefully, I'll rebuild the repository without adding the book.

# How?

I have an old copy of these files, but they are pretty outdated. It's going to
take some time to get it back to its feet. I'll need help from you guys.

# How did you manage to delete the files?

I misused git-filter-repo, which is a tool to rewrite git history. I was trying
to remove the book from the history, but I accidentally removed all files
except the book lol. The misuse happened because of the flag `--invert-paths`,
which is a flag that inverts the paths to be removed.

# Does this mean the book is gone?

Those who is taking this coures have free online access to the book on
[CengClass](https://class.ceng.metu.edu.tr/). Rest can buy it on their
[official website](https://pp4e.online/book.html).
