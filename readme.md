# RIEEE's DataDash

Welcome to DataDash. RIEEE has developed this web application to effectively address the data infrastructure needs of our research partners. DataDash enables RIEEE to deploy and curate a diverse library of web application and database server resources seamlessly.  It ensures security through shibboleth authentication and provides a standard, accessible documentation and access interface for these resources.  To learn more about how this is done and how it benefits research, checkout the Introduction to DataDash dashboard in the Public Dashboards section of the application.

## Development Notes

### July 13th, 2023

- Come back to the idea of unlisted embedded applications if and only if that really seems necessary.  They can always be added as-needed later.

- **Can we get the gmail pfp from logged in users?**  My research on Shibboleth integration suggests we can, so until that's set up, there is a placeholder icon in the eastern header.

- **Digital accessibility policy?** Ask Jeff if he knows anything about complying with https://policy.appstate.edu/Digital_Accessibility

## Instructions

1. Clone the repository:

```shell
git https://github.com/mwhefner/datadash.git
```

2. Navigate to the project directory:

```shell
cd DataDash-application
```

3. Install the required dependencies (optionally, into a virtual environment):

```shell
pip install -r requirements.txt
```

4. Run datadash.py to run the application on http://127.0.0.1:8050/

```shell
python datadash.py
```

## Database Details

https://datadash-admin-dev.appstate.edu/

SQL Credentials:
datadashapp
uXINl[k18bT_5Q(G
