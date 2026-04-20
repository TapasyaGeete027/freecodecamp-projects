test_settings = {
    "Theme" : "Dark",
    "Notification" : "Enabled",
    "Volume" : "High",
    "Language" : "English"
}
def add_setting(setting, item):
    key,value = item
    key = key.lower()
    value = value.lower()
     
    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!" 

def update_setting(setting,item):
    key, value = item
    key = key.lower()
    value = value.lower()  

    if key in setting:
        setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting, key):
    key = key.lower()
    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"        
    else:
        return "Setting not found!"
     
def view_settings(setting):
    if not setting:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in setting.items():
            key = key.capitalize()
            result += f"{key}: {value}\n"
        return result


                 

print(add_setting({'theme':'light'}, ('THEME','dark')))
print(add_setting({'theme':'light'}, ('volume','high')))
print(update_setting({'theme':'light'}, ('theme','dark')))
print(update_setting({'theme':'light'}, ('volume','high')))
print(delete_setting({'theme':'light'}, ('theme')))
print(delete_setting({'theme':'light'}, ('mode')))
print(view_settings({}))
print(view_settings({'theme' : 'light','language' : 'english'}))




  
