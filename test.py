def main():
    print("begin main")
    first()
    print("end main")

def third():
    #print("hello")
    n = int(input(""))
    try:
        print("begin third")
        if n == 1:
            5 / 0
        elif n == 2:
            int("jdgfdkjs")  #ValueError
        else:
            a + b            #NameError
        print("hello")

    #except(ZeroDivisionError,ValueError, NameError)
        #print("exception was handled")

    #except(ZeroDivisionError,ValueError, NameError) as exc:
        #print("exception was handled:", exc.args)     #дает возможность получить ссылку на объект
        #print(exc)
        #print(repr(exc))
        #print(exc.args)
        #print(exc.args[1])

    #except BaseException as exc:
        #print("exception was handled:", exc)

    # except:
        #print("exception was handled")

    except ZeroDivisionError:
        print("exception ZeroDivisionError was handled")
    except ValueError:
        print("exception ValueError was handled")
    except NameError:
        print("exception NameError was handled")

    print("end third")

def second():
    print("begin second")
    third()
    print("end second")

def first():
    print("begin first")
    second()
    print("end first")

main()