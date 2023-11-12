# To make it run every minute

Edit the crontab file by typing:

    crontab -e

Add this line:

    `* * * * * /home/osaa/bunkerbus/em340/get.sh >> /home/osaa/em340data/data.csv`

# To make the data available outside


# Use Google Drive / Google Sheet API

Måske en bedre løsning.

https://developers.google.com/sheets/api/quickstart/python
