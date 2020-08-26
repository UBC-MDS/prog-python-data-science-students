# DSCI-011-prog-python-students

 Student facing repository for MCL-DSCI-011
 
## Updating the Dockerfile & Building a New Image

When one or more Python libraries included in [the `DSCI-011` Dockerfile](https://github.com/UBC-MDS/DSCI-011-prog-python-students/blob/master/dockerfiles/dsci-011/Dockerfile) is/are updated, you may want to create a new image with the new versions. To do this, or make any other type of change to the docker images, such as adding a new Python libraries entirely, follow the steps below:

1. Clone the `DSCI-011-prog-python-students` repo
2. Open the Dockerfile you wish to edit using a text editor of your choice
3. Edit the Dockerfile as you wish. If you are adding new Python libraries to the `dsci-011` Dockerfile, you will want to add the library and specify the version under this line: `RUN conda install --quiet --yes -c conda-forge \ ...`. To change a version number, simply change the version number that comes after the package name. Instructions on how to specify certain versions with `conda` can be found [here](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/)
4. Commit & push your changes. This will trigger a GitHub workflow that will automatically bump the version, create a Git tag and GitHub release, build the images, and publish them [on DockerHub](https://hub.docker.com/u/ubcstat) with the same tag as in the Git tag and the GitHub release. 
   - **The commit message is used to determine the level of the version that should be bumped.** For instructions on how to change the level of the version that is bumped, [see here](https://github.com/anothrNick/github-tag-action#bumping). For example, if the current version is 1.2.3, and you push a commit that includes `#patch`, the GitHub workflow will generate version 1.2.4 as the next release.
5. Wait for the docker images to be built!
