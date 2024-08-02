import os
import streamlit as st


def rename_filenames_and_folders(root_dir, old_name, new_name):
    for subdir, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            if old_name in name:
                old_file_path = os.path.join(subdir, name)
                new_file_path = os.path.join(subdir, name.replace(old_name, new_name))
                os.rename(old_file_path, new_file_path)
                st.write(f'Renamed file: {old_file_path} to {new_file_path}')

        for name in dirs:
            if old_name in name:
                old_dir_path = os.path.join(subdir, name)
                new_dir_path = os.path.join(subdir, name.replace(old_name, new_name))
                os.rename(old_dir_path, new_dir_path)
                st.write(f'Renamed directory: {old_dir_path} to {new_dir_path}')


def rename_text_inside_files(root_dir, old_text, new_text):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if old_text in content:
                updated_content = content.replace(old_text, new_text)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                st.write(f'Updated text in: {file_path}')


def rename_everything(root_dir, old_name, new_name):
    rename_filenames_and_folders(root_dir, old_name, new_name)
    rename_text_inside_files(root_dir, old_name, new_name)


def main():
    st.title('Renamer Master')

    st.header('Rename Filenames, Folders, and Text Inside Files')
    root_directory = st.text_input("Enter the root directory path:")
    old_name = st.text_input("Enter the old name or text to be replaced:")
    new_name = st.text_input("Enter the new name or text:")

    if st.button('Rename Everything'):
        if root_directory and old_name and new_name:
            if os.path.isdir(root_directory):
                rename_everything(root_directory, old_name, new_name)
            else:
                st.warning("The specified root directory does not exist.")
        else:
            st.warning("Please enter the root directory, old name, and new name.")


if __name__ == '__main__':
    main()
