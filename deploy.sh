#!/bin/sh -l

set -e

if [ -z "$ACCESS_TOKEN" ] && [ -z "$GITHUB_TOKEN" ]
then
  echo "You must provide the action with either a Personal Access Token or the GitHub Token secret in order to deploy."
  exit 1
fi

if [ -z "$BRANCH" ]
then
  echo "You must provide the action with a branch name it should deploy to, for example gh-pages or docs."
  exit 1
fi



case "$FOLDER" in /*|./*)
  echo "The deployment folder cannot be prefixed with '/' or './'. Instead reference the folder name directly."
  exit 1
esac

# Gets the commit email/name if it exists in the push event payload.
COMMIT_EMAIL=`jq '.pusher.email' ${GITHUB_EVENT_PATH}`
COMMIT_NAME=`jq '.pusher.name' ${GITHUB_EVENT_PATH}`

# If the commit email/name is not found in the event payload then it falls back to the actor.
if [ -z "$COMMIT_EMAIL" ]
then
  COMMIT_EMAIL="${GITHUB_ACTOR:-github-pages-deploy-action}@users.noreply.github.com"
fi

if [ -z "$COMMIT_NAME" ]
then
  COMMIT_NAME="${GITHUB_ACTOR:-GitHub Pages Deploy Action}"
fi

echo "change directory"
# Directs the action to the the Github workspace.
cd $GITHUB_WORKSPACE/build && \

# Configures Git.
echo "git init"
git init && \
git config --global user.email "${COMMIT_EMAIL}" && \
git config --global user.name "${COMMIT_NAME}" && \
echo "configured"

## Initializes the repository path using the access token.
REPOSITORY_PATH="https://${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" && \
echo "Initializes the repository path using the access token"

# Checks to see if the remote exists prior to deploying.
# If the branch doesn't exist it gets created here as an orphan.
if [ "$(git ls-remote --heads "$REPOSITORY_PATH" "$BRANCH" | wc -l)" -eq 0 ];
then
  echo "Creating remote branch ${BRANCH} as it doesn't exist..."
  git checkout "${BASE_BRANCH:-master}" && \
  git checkout --orphan $BRANCH && \
  git rm -rf . && \
  touch README.md && \
  git add README.md && \
  git commit -m "Initial ${BRANCH} commit" && \
  git push $REPOSITORY_PATH $BRANCH
fi

echo "try to check out"
# Checks out the base branch to begin the deploy process.
git remote update
git fetch --all
echo ${GITHUB_REPOSITORY}
echo git branch -a

echo ${BASE_BRANCH:-master}

git checkout "${BASE_BRANCH:-master}" && \
echo "checked out"

# Commits the data to Github.
echo "Deploying to GitHub..." && \
git add -f $FOLDER && \

git commit -m "Deploying to ${BRANCH} from ${BASE_BRANCH:-gh-pages} ${GITHUB_SHA}" --quiet && \
git push $REPOSITORY_PATH `git subtree split --prefix $FOLDER ${BASE_BRANCH:-master}`:$BRANCH --force && \

echo "Deployment succesful!"
