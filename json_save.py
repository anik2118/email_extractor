def save(anik,filename,folder_path,json,os,list_of_printed_cars):         

        list_of_printed_cars.append(anik)
        folder_path = r"D:\email_extraction project"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Specify the file path within the folder
        file_path = os.path.join(folder_path, filename)
        # Define the path to the JSON file
            # Write the place information to the JSON file
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(list_of_printed_cars, json_file, indent=4)
        print(list_of_printed_cars)
        print(f"Place information has been written to {filename}")
