from app.calculation import CalculationFactory


HELP_TEXT = """Commands:
  add <a> <b>        Addition
  subtract <a> <b>   Subtraction
  multiply <a> <b>   Multiplication
  divide <a> <b>     Division

Special:
  help              Show this message
  history           Show calculation history
  exit              Exit the program
"""


class Calculator:
    def __init__(self):
        self.history = []

    @staticmethod
    def is_number(value: str) -> bool:
        # EAFP：尝试转换，失败就捕获
        try:
            float(value)
            return True
        except ValueError:
            return False

    def run(self, input_func=input, output_func=print):
        output_func("Type 'help' for instructions.")

        while True:
            raw = input_func(">> ").strip()

            # LBYL：空输入先检查
            if not raw:
                output_func("Please enter a command.")
                continue

            cmd = raw.lower()

            # special commands
            if cmd == "help":
                output_func(HELP_TEXT)
                continue

            if cmd == "history":
                if not self.history:
                    output_func("No history yet.")
                else:
                    for item in self.history:
                        output_func(item)
                continue

            if cmd == "exit":
                output_func("Goodbye!")
                break

            parts = raw.split()

            # LBYL：格式检查
            if len(parts) != 3:
                output_func("Invalid format. Use: <operation> <a> <b>")
                continue

            op, a_str, b_str = parts

            # LBYL：数字检查
            if not self.is_number(a_str) or not self.is_number(b_str):
                output_func("Invalid numbers. Please enter numeric values.")
                continue

            try:
                # EAFP：有风险的步骤放在 try 里
                a = float(a_str)
                b = float(b_str)

                calc = CalculationFactory.create(op, a, b)
                result = calc.get_result()

                record = f"{op.lower()} {a} {b} = {result}"
                self.history.append(record)

                output_func(str(result))

            except ZeroDivisionError as e:
                output_func(f"Error: {e}")
            except ValueError as e:
                output_func(f"Error: {e}")
            except Exception as e:
                output_func(f"Unexpected error: {e}")
