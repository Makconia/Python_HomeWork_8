import view
import database


def main():
    match view.get_op():
        case '0' | '' | ' ':
            view.print_completed() 
        case '1':
            database.import_data() 
            next_action()
        case '2':
            database.export_data() 
            next_action()
        case '3':
            database.delete_data() 
            next_action()
        case '4':
            database.change_data() 
            next_action()
        case '5':
            database.sorted() 
            next_action()
        case _:
            view.print_error() 
            main()


def next_action():
    if view.get_next_action() != '0':
        main()
    else: view.print_completed()

if __name__ == "__main__":
    main()