from gitlab import Gitlab as gl
from git import Git as git
from getpass import getpass as gp
from pathlib import Path
from os import mkdir


def path_info():
    base_path = Path().resolve()
    repos_path = input("Enter name for directory where you want to find your repos"
                       "(Directory will be created if it's not present!): ")
    new_path = f"{base_path}\\{repos_path}"
    return new_path


def directory_creation(path):
    try:
        mkdir(path)
    except FileExistsError:
        choice = input("Directory exists. Do you want to save files there or start again ?"
                       "Valid options: y or yes: ")
        if choice.lower() == "y" or "yes":
            directory_creation(path_info())
    return path


def main():
    # Retrieving GitLab credentials from user
    gl_host = input("Enter your GitLab url: ")
    gl_access_token = gp("Enter your Access token: ")
    gl_group_id = int(input("Enter group ID: "))
    repos_directory = directory_creation(path_info())

    # Connecting to GitLab Host and getting list of all repositories from provided group
    gl_connect = gl(gl_host, private_token=gl_access_token)
    gl_group = gl_connect.groups.get(gl_group_id)
    projects_group = gl_group.projects.list(iterator=True)

    project_counter = 1
    for project in projects_group:
        print(f"[{project_counter}] - cloning {project.name}")
        git(repos_directory).clone(project.ssh_url_to_repo)
        project_counter += 1

    print(f"You've successfully cloned {project_counter - 1} project repositories")


if __name__ == "__main__":
    main()
