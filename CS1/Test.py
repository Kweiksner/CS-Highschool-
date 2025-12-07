def decimal(number):
        try:
            if '/' in number:
                parts = number.split('/')#splits word into 
                if len(parts) == 2:
                    numerator = float(parts[0])
                    denominator = float(parts[1])
                    if denominator != 0:
                        return numerator / denominator
                    else:
                        return "False"
            return int(number)
        except:
            try:
                return float(number)
            except:
                return "False"

def main():
    numb  = "3/1"
    print(decimal(numb))

main()