# gitlab_group_clone

### Description:

This is simple Python script that clones all projects from provided GitLab group

### Usage:


Script will retrieve values from console input and store it into variables

    - repos_path : Name of directory where user wants to store projects. If directory doesn't exist it will be created
    - gl_host: URL of GitLab server (ex: https://gitlab.mydomain.com)
    - gl_access_token: Your Acces Token for GitLab authentication
    - gl_group_id : Group ID on GitLab (this integer can be found bellow Group name in browser)