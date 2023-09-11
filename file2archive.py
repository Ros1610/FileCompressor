import zipfile

import PySimpleGUI as sg
from zip_creator import make_archive
from zip_extractor import extract_archive


def file2archive():
    """Link to the extractor"""
    extract_button0 = sg.Button("Archive2File")

    label10 = sg.Text("Files:")
    input10 = sg.Input()
    choose_button10 = sg.FilesBrowse("Browse")

    label20 = sg.Text("Destination directory:")
    input20 = sg.Input()
    choose_button20 = sg.FolderBrowse("Browse")

    compress_button = sg.Button("Compress")
    output_label0 = sg.Text(key="output0", text_color="white")

    window0 = sg.Window("File2Archive",
                        layout=[[extract_button0], [label10, input10, choose_button10],
                               [label20, input20, choose_button20], [compress_button, output_label0]])
    while True:
        event, value = window0.read()

        try:
            """Get filepaths from event values, split filepaths into a list"""
            filepaths = value["Browse"].split(";")
            folder = value["Browse0"]

        except IndexError:
            pass

        except TypeError:
            pass

        except AttributeError:
            pass

        match event:
            case "Compress":
                try:
                    make_archive(filepaths, folder)
                    window0["output0"].update(value="Compression completed!")

                except FileNotFoundError:
                    sg.popup("The file hasn't been found")

            case "Archive2File":
                window0.close()
                archive2file()

            case sg.WIN_CLOSED:
                break

    window0.close()


def archive2file():
    """Link to the compressor"""
    compress_button1 = sg.Button("File2Archive")

    label11 = sg.Text("Archive: ")
    input11 = sg.Input()
    choose_button11 = sg.FileBrowse("Browse", key="archive")

    label21 = sg.Text("Destination directory: ")
    input21 = sg.Input()
    choose_button21 = sg.FolderBrowse("Browse", key="folder")

    extract_button1 = sg.Button("Extract")
    output_label1 = sg.Text(key="output1", text_color="white")

    window1 = sg.Window("Archive2File",
                        layout=[[compress_button1],[label11, input11, choose_button11],
                                [label21, input21, choose_button21],
                                [extract_button1, output_label1]])

    while True:
        event, value = window1.read()
        match event:
            case "Extract":
                try:
                    archive_path = value["archive"]
                    dest_dir = value["folder"]
                    extract_archive(archive_path, dest_dir)
                    window1["output1"].update(value="Extraction completed!")

                except zipfile.BadZipFile:
                    sg.popup("Select a zip file")

                except FileNotFoundError:
                    sg.popup("The file hasn't been found")

            case "File2Archive":
                window1.close()
                file2archive()

            case sg.WIN_CLOSED:
                break

    window1.close()


file2archive()
