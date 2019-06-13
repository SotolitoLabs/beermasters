# Poor Man's CI
We don't want to depend on third party services for our CI

## (SERVER) Create a bare git repository in the production server
We need this in order to trigger the `post-recieve` hook

```
$ git init --bare /var/beer/ci-update-repo
```

## (SERVER) Add the post recieve script

```
$ cd ci-update-repo/hooks
$ cat <<EOF >> post-recieve
#!/usr/bin/sh
# Just pull on the repo
REPODIR="/home/repo"
cd $REPODIR
git pull
EOF
```

## (WORKSTATION) Add server bare repo as remote

```
$ cd git-local-repo
$ git add remote ci-repo  user@remote.repo.com
```

## (WORKSTATION) Trigger the CI
After we make changes and commit them push them to the CI

```
$ git push ci-repo master
```

**Be Happy!!**


# References
* https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa