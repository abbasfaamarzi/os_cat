from oscat.note_files import CatNoteBook
class CatTreeProperties:
    work_space_name = "PycharmProjects"
    cats_space_name = "\cats"
    dcat_space = "\data_cat"
    ccat_space = "\crypto_cat"

    space_files = {
        "cc" : {
            "cat_key_maker" : "#hi,cats"
        },
        "dc": {
            "models": "#hi,models cats",
            "serializer": "#hi,serializer cats",
            "views": "#hi,views cats",
        }
    }
    cat_os_main_dirs = {
        '.idea',
        '.git',
        'LICENSE',
        'setup.py',
        'workflow.yml',
        'requirements.txt',
        'README.md',
    }
    tree_key_word = ['curser_items', 'status', 'target']
    note_book = CatNoteBook
