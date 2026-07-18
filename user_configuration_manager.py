# Dictionary containing the default user settings
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

# Function to add a new setting to the dictionary
def add_setting(settings_dict: dict, settings_tup: tuple) -> str:
    # Convert the key and value to lowercase for consistency
    key = settings_tup[0].lower()
    value = settings_tup[1].lower()

    # Check if the setting already exists
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    # Add the new setting
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Function to update an existing setting
def update_setting(settings_dict, settings_tup):
    # Convert the key and value to lowercase
    key, value = settings_tup
    key = key.lower()
    value = value.lower()

    # Check if the setting exists before updating
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    # Return an error if the setting is not found
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Function to delete a setting
def delete_setting(settings_dict, settings_key):
    # Convert the key to lowercase
    key = settings_key.lower()

    # Delete the setting if it exists
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"

    # Return an error if the setting is not found
    return "Setting not found!"

# Function to display all settings
def view_settings(settings_dict):
    # Check if the dictionary is empty
    if not settings_dict:
        return "No settings available."

    # Create the heading for the output
    result = "Current User Settings:\n"

    # Loop through all settings and add them to the output
    for key, value in settings_dict.items():
        result += f"{key.capitalize()}: {value}\n"

    # Return the formatted settings
    return result