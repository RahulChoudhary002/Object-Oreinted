class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error evaluating expression: {e}"

    def display_result(self):
        result = self.evaluate()
        print(f"Expression: {self.expression}")
        print(f"Result: {result}")

if __name__ == "__main__":
    user_input = input("Enter a mathematical expression (e.g., 3 + 4 * 2): ")
    solver = ExpressionSolver(user_input)
    solver.display_result()
