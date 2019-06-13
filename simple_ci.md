# Poor Man's CI
We don't want to depend on third party services for our CI

## (SERVER) Create a bare git repository in the production server
We need this in order to trigger the `post-recieve` hook

```
$ git init --bare /var/beer/ci-update-repo
```

## (SERVER) Add the post recieve script
This can be as easy as issuing a `git pull` or as complex as creating packages, containers
and running smoke tests.

```
$ cd ci-update-repo/hooks
$ cat <<EOF >> post-recieve
#!/usr/bin/sh
# Just pull on the repo
REPODIR="/home/repo"
cd $REPODIR
echo "TRIGGERING POOR MAN's CI" >> $REPODIR/ci.log
git pull
EOF
```

## (WORKSTATION) Add server bare repo as remote

```
$ cd git-local-repo
$ git remote add ci-repo ssh://user@remote.repo.com:1234/var/beer/ci-update-repo
```

## (WORKSTATION) Trigger the CI
After we make changes and commit them push them to the CI

```
$ git push ci-repo master
```

**Be Happy!!**


# References
* https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa
