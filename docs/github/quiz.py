"""GitHub and contributing quiz answers."""

# # GitHub

# ## 1.1 What is GitHub?

# GitHub is a web-based hosting platform for Git repositories. It stores
# repositories in the cloud and adds a collaboration layer on top of Git:
# issues, pull requests, code review, discussions, wikis, project boards, CI/CD
# (GitHub Actions) and access control. It is where most open source projects
# live and where teams work on code together.

# ## 1.2 How is GitHub related to Git?

# Git is the version control system itself: a command line tool that runs
# locally and tracks changes to files. GitHub is a service that hosts Git
# repositories remotely.
#
# - Git works without GitHub.
# - GitHub cannot exist without Git.
# - GitHub is one of many hosts (others: GitLab, Bitbucket).
#
# Git is the engine, GitHub is the garage and the social network around it.

# ## 1.3 How does forking a repository differ from cloning it?

# **Clone** copies a repository from a remote server to MY **local machine**:
#
# ```bash
# git clone <url>
# ```
#
# I get a local copy. If I do not have write access to the original repository,
# I cannot push to it.
#
# **Fork** creates a copy of someone else's repository
# **under MY own GitHub account** (server side, done through the GitHub UI). I
# have full write access to my fork.
#
# Standard open source flow:
#
# 1. Fork the upstream repository.
# 2. Clone **MY fork** locally.
# 3. Create a branch and commit MY changes.
# 4. Push the branch to MY fork.
# 5. Open a pull request from MY fork to the upstream repository.

# ## 1.4 Why are pull requests needed and how do they work?

# A pull request (PR) proposes that my changes be merged into another branch or
# repository. It exists so that changes can be
# **reviewed, discussed and tested** before entering the main codebase, instead
# of anyone pushing directly to `main`.
#
# How it works:
#
# 1. Create a branch and commit my changes.
# 2. Push the branch to GitHub.
# 3. Open a PR: choose the base branch (for example `upstream/main`) and the
#    compare branch (my branch).
# 4. GitHub shows a diff, and automated checks (CI, linters) run.
# 5. Reviewers comment, request changes or approve.
# 6. I push more commits to the same branch and the PR updates automatically.
# 7. A maintainer merges it.
#
# If the PR description contains `Closes <issue-url>`, the linked issue is
# closed automatically on merge.

# ## 1.5 Does GitHub use your email address to link commits to your account?

# Yes. Every Git commit records an author email taken from
# `git config user.email`. GitHub matches that email against the verified
# emails on your account.
#
# - If it matches, the commit is attributed to your profile and counts toward
#   my contribution graph.
# - If it does not match, the commit still appears in the history but is not
#   linked to my account: no avatar, no contribution credit.
#
# ```bash
# git config user.email
# ```
#
# The value must be one of the emails added to your GitHub account settings.

# ## 1.6 Which command generates an SSH key for SSH access to a repository?

# ```bash
# ssh-keygen -t ed25519 -C "your_email@example.com"
# ```
#
# Legacy alternative:
#
# ```bash
# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# ```
#
# This creates a private key (`~/.ssh/id_ed25519`) and a public key
# (`~/.ssh/id_ed25519.pub`). The **public** key is then added to GitHub under
# Settings -> SSH and GPG keys.

# # Contributing to projects

# ## 2 Create an issue `UPDATE README` with a task list in the description.

# https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/issues/746

# ## 2.1 What do you do to create a fork? Paste the link to your fork.

# Click **Fork** at the top right of the repository page, then **Create fork**.
#
# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course

# ## 2.2 Create a `dev` branch in your fork and paste the link.

# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/tree/dev

# ## 2.3 Add https://t.me/RuslanSenatorov to the README in `dev` and commit.

# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/commit/8725f56

# ## 2.4 Open a pull request with your own branch as the target.

# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/pull/1

# ## 2.5 Comment on the pull request, submit the review and add a second link.

# I left the comment «ок» on the **Files changed** tab and clicked
# **Submit review**, then added https://t.me/SENATOROVAI to the README.
#
# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/commit/3d3f3fd

# ## 2.6 Merge the pull request and paste the link.

# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/pull/1

# ## 2.7 Paste the link to the closed pull requests in the repository.

# https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/pulls?q=is%3Apr+is%3Aclosed

# ## 2.8 How do you see the files in a repository at a given commit?

# Open the commit and click **Browse files**. The commit hash is then shown at
# the top left instead of a branch name.
#
# https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/tree/3d3f3fdb300a67da17c946b1b76f5799ad4d6598

# ## 2.9 How do you open a pull request against another pull request, and why?

# When opening the pull request, choose the other pull request's branch as the
# **base** branch instead of `main`. It is useful for proposing changes to
# someone else's open pull request, or for splitting a large change into
# smaller steps that are reviewed one after another.

# # GitHub workflow

# ## 3 List the 8 steps for contributing to someone else's project.

# 1. Fork the project.
# 2. Create a topic branch from the main branch.
# 3. Make commits that improve the project.
# 4. Push the branch to my fork.
# 5. Open a pull request.
# 6. Discuss it and keep committing if changes are needed.
# 7. The project owner merges or closes the pull request.
# 8. Sync the updated main branch back to my fork.

# ## 3.1 What makes an issue close automatically?

# - **Pull request:** put a closing keyword and the issue in the description,
#   for example `Closes #12`. The issue closes when the pull request is merged
#   into the default branch.
# - **Commit:** put the same keyword in the commit message. The issue closes
#   when the commit reaches the default branch.
#
# The keywords are `close`, `fix` and `resolve` and their other forms, such as
# `Closes` and `Fixes`.

# ## 3.2 How do you reject or close a pull request? Attach a screenshot.

# Open the pull request on the **Conversation** tab, scroll to the bottom and
# click **Close pull request**. This closes it without merging.
#
# ![Close pull request button](images/close-pr.png)

# ## 3.3 Do you need to create an issue before sending a pull request?

# GitHub does not require it, and a pull request can be opened without one.
# Many projects do ask for it. For example, the CatBoost `CONTRIBUTING.md` asks
# contributors to discuss an idea in an issue first.

# ## 3.4 Which tab shows the list of changes in a pull request?

# **Files changed**.

# ## 3.5 Which tab holds the pull request discussion?

# **Conversation**.

# # Creating a pull request

# ## 4 Can you open a pull request if you changed nothing in your fork?

# No. If the branch has no differences from the target branch, GitHub does not
# let me create a pull request, because there is nothing to compare.

# ## 4.1 What do you need to do to open a pull request?

# Push the branch to my fork, then click **Compare & pull request** (or
# **New pull request**). Choose the base and compare branches, write the title
# and description, and click **Create pull request**.

# ## 4.2 What do you do if your fork is out of date?

# Update it from the original repository: click **Sync fork** on GitHub, or
# run:
#
# ```bash
# git remote add upstream <original-repo-url>
# git fetch upstream
# git switch main
# git merge upstream/main
# git push origin main
# ```

# ## 4.3 What do you do if a pull request has merge conflicts?

# Update my branch from the target branch, resolve the conflicts, commit and
# push:
#
# ```bash
# git fetch upstream
# git merge upstream/main
# git add <fixed-files>
# git commit
# git push
# ```
#
# The pull request updates by itself. Simple conflicts can also be solved on
# GitHub with the **Resolve conflicts** button.

# # Code snippets and quoting

# ## 5 How do you add a code snippet to an issue comment?

# Put the code between lines of three backticks, with the language name after
# the opening ones:
#
# ````markdown
# ```python
# print("Hello, GitHub!")
# ```
# ````

# ## 5.1 Which key inserts the selected text into a comment as a quote?

# The `r` key.

# ## 5.2 How do you insert an image into an issue?

# Drag the file into the comment box, paste it with `Ctrl+V`, or click the
# attach files button below the box.

# # Keeping a repository up to date

# ## 6 How do you know that your fork is out of date?

# The fork's page on GitHub shows **This branch is N commits behind**. In the
# terminal:
#
# ```bash
# git fetch upstream
# git log --oneline HEAD..upstream/main
# ```

# ## 6.1 How do you update a fork?

# Click **Sync fork**, then **Update branch** on the fork's page. In the
# terminal, use the commands from 4.2.

# # Adding collaborators

# ## 7 How do you add collaborators to a repository?

# Open **Settings**, then **Collaborators**, click **Add people** and enter the
# person's GitHub username or email. They get access after accepting the
# invitation.

# # Mentions and notifications

# ## 8 Which character mentions a user?

# `@`, for example `@nysib`.

# ## 8.1 Where is the notification center? Give the link.

# https://github.com/notifications

# # Special files

# ## 9 What is a README file and why is it needed?

# It is the text file in the root of a repository that GitHub shows on the main
# page. It explains what the project is, how to install and use it, and where
# to find more information.

# ## 9.1 What is a CONTRIBUTING file and why is it needed?

# It describes how to contribute to the project, such as how to report bugs and
# what a pull request should look like. GitHub links to it when someone opens
# an issue or a pull request.

# # Project management

# ## 10 How do you change the default branch?

# Open **Settings**, then **General**, go to **Default branch**, click the
# switch branch button, choose the branch and click **Update**.

# ## 10.1 How do you transfer a project to another owner? Which button does it?

# Open **Settings**, then **General**, go to the **Danger Zone** at the bottom
# and click **Transfer**.

# ## 10.2 What is a `.gitignore` file?

# It lists files and folders that Git should not track, such as virtual
# environments, caches and local settings. Files that are already tracked are
# not affected.
