# Deployment Notes:

## Port number of your server:
* Your Team Number determines which port you are ALLOWED to use.
* For example, if your Team Number = 3, server port number should be `5030`
* If your Team number = 5, server port number should be `5050`
* In general, given Team Number `X`, server port should be `50X0`

## Change  `Dockerfile` content according to your server port:

Inside your `Dockerfile` content, change following lines to your server port:

```Dockerfile
# Expose the port the Flask app runs on
EXPOSE 5010
```

## Set up Secrets in Gtihub repository:
* Go to `Repository Settings` -> `Secrets and Variables` -> `Actions`
* Add following secrets:
  * `DEPLOY_KEY`: copy and paste the content of SSH key (spm24.pem)
  * `SERVER_IP`: ip address of the server: `20.163.29.111`
  * `SERVER_USER`: server username `azureuser`


## Edit worklow file `.github/workflows/deploy.yml` in your repo:

* Change all of the container name to your own teams unique container:
  * Search and replace all of the occurances of `spm24_project0` with your teams number (for example: `spm24_project3` if your team number is 3)
  * Search and replace port number `5001`, replace it with `50X1` (for example: `5031`, if your team number is 3)
  * Search and replace port number `5000`, replace it with `50X0` (for example: `5030`, if your team number is 3)

## Merge your changes to the main branch

* Create pull request to merge your changes to the `main` branch, and merge them (resolve conflicts if necessary)
* Monitor `Github Actions` logs
* After successfull deployment, test your server in `http://20.163.29.111:50X0` (`50X0` is your own port number)
