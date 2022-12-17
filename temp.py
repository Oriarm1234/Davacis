def sanitizedInput(message,desiredType=None,valMin=None,valMax=None):
    while True:
        userInput = input(message)
        if desiredType != None:
                try:
                    userInput = type(desiredType)(userInput)
                except ValueError:
                    match desiredType:
                        case "int":
                            hrData = "an integer"
                        case "str":
                            hrData = "a character"
                        case "float":
                            hrData = "a number" 
                        case "bool":
                            hrData = "'1' or '0'"
                        case other:
                            logging.ERROR(f"{desiredType} is not a handled type")
                            raise SyntaxError
                    print(f"Invalid data, please enter {hrData}.") # possibly go fuck yourself pylance
                    continue
        if valMin != None:
            if isinstance(userInput,int) or isinstance(userInput,float):
                if valMin > userInput: 
                    print(f"Please enter a value greater than {valMin}.")
                    continue
            elif isinstance(userInput,str):
                if valMin > len(userInput):
                    print(f"Please enter a value longer than {valMin} characters.")
                    continue
        if valMax != None:
            if isinstance(userInput,int) or isinstance(userInput,float):
                if valMax < userInput: 
                    print(f"Please enter a value less than {valMin}.")
                    continue
            elif isinstance(userInput,str):
                if valMax < len(userInput):
                    print(f"Please enter a value shorter than {valMin} characters.")
                    continue
        break
    