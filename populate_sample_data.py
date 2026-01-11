"""
Management command to populate sample C++ missions into the database.
Usage: python manage.py shell < populate_sample_data.py
Or: ./venv/bin/python manage.py shell < populate_sample_data.py
"""

from game.models import Question, Option

# Clear existing data (optional)
Question.objects.all().delete()

# Mission 1: Variables & Data Types
q1 = Question.objects.create(
    story="""Robo-X is starting its programming journey! It needs to understand how variables work in C++.
    
    The robot must store its battery level (90) in a variable. Which line correctly declares and initializes this?""",
    code="""#include <iostream>
using namespace std;

int main() {
    // Line to complete:
    cout << battery << endl;
    return 0;
}""",
    hint="Variables in C++ need a data type (int, float, char, etc.) and can be initialized with a value.",
    order=1
)

Option.objects.create(question=q1, text="int battery 90;", is_correct=False)
Option.objects.create(question=q1, text="int battery = 90;", is_correct=True)
Option.objects.create(question=q1, text="battery int = 90;", is_correct=False)
Option.objects.create(question=q1, text="variable battery = 90;", is_correct=False)

# Mission 2: Loops
q2 = Question.objects.create(
    story="""Robo-X needs to process 5 sensor readings in sequence. To avoid writing the same code 5 times, 
    it should use a loop. Which loop will correctly iterate 5 times (0 to 4)?""",
    code="""#include <iostream>
using namespace std;

int main() {
    // Loop needed here
    cout << "Reading sensor " << i << endl;
    return 0;
}""",
    hint="A for loop with condition i < 5 will execute exactly 5 times when starting from i = 0.",
    order=2
)

Option.objects.create(question=q2, text="for(int i = 0; i < 5; i++)", is_correct=True)
Option.objects.create(question=q2, text="for(int i = 1; i <= 5; i++)", is_correct=False)
Option.objects.create(question=q2, text="while(i < 5)", is_correct=False)
Option.objects.create(question=q2, text="for(int i = 0; i <= 5; i++)", is_correct=False)

# Mission 3: Arrays
q3 = Question.objects.create(
    story="""Robo-X has 5 sensors and wants to store all their readings. 
    An array is perfect for this! How do you declare an array of 5 integers named 'sensors'?""",
    code="""#include <iostream>
using namespace std;

int main() {
    // Array declaration needed
    sensors[0] = 45;
    sensors[1] = 67;
    cout << sensors[0] << endl;
    return 0;
}""",
    hint="Arrays are declared with [size] after the variable name. The size represents how many elements it can hold.",
    order=3
)

Option.objects.create(question=q3, text="array sensors[5];", is_correct=False)
Option.objects.create(question=q3, text="int[5] sensors;", is_correct=False)
Option.objects.create(question=q3, text="int sensors[5];", is_correct=True)
Option.objects.create(question=q3, text="sensors int = [5];", is_correct=False)

# Mission 4: Functions
q4 = Question.objects.create(
    story="""Robo-X needs to perform the same calculation repeatedly - adding 10 to a number. 
    It's time to learn functions! Which function signature correctly defines a function that adds 10 to a number?""",
    code="""#include <iostream>
using namespace std;

// Function definition needed

int main() {
    int result = add10(25);
    cout << result << endl; // Should print 35
    return 0;
}""",
    hint="Functions need: return type, function name, parameters in parentheses, and a body in curly braces.",
    order=4
)

Option.objects.create(question=q4, text="int add10(int x) { return x + 10; }", is_correct=True)
Option.objects.create(question=q4, text="add10(int x) { return x + 10; }", is_correct=False)
Option.objects.create(question=q4, text="int add10 x { return x + 10; }", is_correct=False)
Option.objects.create(question=q4, text="function add10(x) { return x + 10; }", is_correct=False)

# Mission 5: Conditionals
q5 = Question.objects.create(
    story="""Robo-X's battery level affects its behavior. If battery > 50%, it works at full speed. 
    Otherwise, it works slowly. Which if-else statement implements this logic?""",
    code="""#include <iostream>
using namespace std;

int main() {
    int battery = 60;
    
    // Conditional logic needed
    
    return 0;
}""",
    hint="Use if(condition) for the first check and else for the alternative. The condition battery > 50 checks if it's greater than 50.",
    order=5
)

Option.objects.create(question=q5, text="if(battery > 50) { cout << \"Full speed\"; } else { cout << \"Slow\"; }", is_correct=True)
Option.objects.create(question=q5, text="if(battery = 50) { cout << \"Full speed\"; }", is_correct=False)
Option.objects.create(question=q5, text="if battery > 50 cout << \"Full speed\";", is_correct=False)
Option.objects.create(question=q5, text="if(battery < 50) { cout << \"Full speed\"; } else { cout << \"Slow\"; }", is_correct=False)

# Mission 6: Strings
q6 = Question.objects.create(
    story="""Robo-X needs to store and display messages like "Hello World!". 
    In C++, text is stored in strings. How do you declare a string variable?""",
    code="""#include <iostream>
#include <string>
using namespace std;

int main() {
    // String declaration needed
    message = "Hello Robo-X!";
    cout << message << endl;
    return 0;
}""",
    hint="The <string> header provides the string type in C++. Declare it like: string variableName;",
    order=6
)

Option.objects.create(question=q6, text="string message;", is_correct=True)
Option.objects.create(question=q6, text="char message;", is_correct=False)
Option.objects.create(question=q6, text="text message;", is_correct=False)
Option.objects.create(question=q6, text="str message;", is_correct=False)

# Mission 7: Pointers
q7 = Question.objects.create(
    story="""Robo-X learns about memory! A pointer stores the address of a variable in memory. 
    If x = 42, how do you create a pointer that points to x?""",
    code="""#include <iostream>
using namespace std;

int main() {
    int x = 42;
    // Pointer declaration needed
    cout << *ptr << endl; // Should print 42
    return 0;
}""",
    hint="The & operator gets the address of a variable. A pointer is declared with * and assigned with the & operator.",
    order=7
)

Option.objects.create(question=q7, text="int* ptr = &x;", is_correct=True)
Option.objects.create(question=q7, text="int ptr = *x;", is_correct=False)
Option.objects.create(question=q7, text="int* ptr = x;", is_correct=False)
Option.objects.create(question=q7, text="pointer ptr = &x;", is_correct=False)

# Mission 8: Classes & Objects
q8 = Question.objects.create(
    story="""Robo-X becomes advanced! It learns Object-Oriented Programming. 
    A class is a blueprint for objects. How do you create a simple class definition?""",
    code="""// Class definition needed

int main() {
    Robot robo; // Create an object
    return 0;
}""",
    hint="A class is defined with the 'class' keyword, followed by the class name and a body inside curly braces.",
    order=8
)

Option.objects.create(question=q8, text="class Robot { };", is_correct=True)
Option.objects.create(question=q8, text="class Robot { }:;", is_correct=False)
Option.objects.create(question=q8, text="Robot class { };", is_correct=False)
Option.objects.create(question=q8, text="define Robot class { };", is_correct=False)

print("✅ Sample data loaded successfully!")
print("8 C++ missions have been added to your database.")
print("\nYou can now:")
print("1. Go to http://127.0.0.1:8000/game/ to see all missions")
print("2. Create a user account to take the quizzes")
print("3. Test the full MVT flow!")
