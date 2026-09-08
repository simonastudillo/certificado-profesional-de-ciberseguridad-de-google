def display_investigation_message():
   print("investigate activity")

application_status = "potential concern"
email_status = "okay"

if application_status == "potential concern":
   print("application_log:")
   display_investigation_message()

if email_status == "potential concern":
   print("email log:")