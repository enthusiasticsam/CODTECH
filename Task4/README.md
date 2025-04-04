#Task-4 OPTIMIZATION MODEL#

COMPANY: CODTECH IT SOLUTIONS

NAME: SHAIK SAMEENA

INTERN ID: CT08VQW

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

This project is a linear programming optimization model designed to help businesses maximize profit by determining the optimal production plan for two products, Product A and Product B. Using Python and the PuLP library, we formulate a mathematical model that takes into account key constraints such as material availability and labor hours. The goal is to decide how many units of each product should be produced to achieve the highest possible profit while ensuring that resources are not exceeded. Product A generates a profit of $40 per unit, while Product B contributes $30 per unit. However, production is limited by the available 100 units of material and 80 labor hours. Each unit of Product A requires 4 units of material and 2 labor hours, whereas Product B consumes 3 units of material and 4 labor hours per unit.

To solve this problem, we define decision variables representing the number of units produced for each product. The objective function, which we aim to maximize, is the total profit expressed as Profit = 40A + 30B. Constraints are then formulated to ensure that the production plan does not exceed the available resources. The material constraint is represented as 4A + 3B ≤ 100, while the labor constraint is 2A + 4B ≤ 80. Additionally, a non-negativity constraint is applied, ensuring that the number of products produced cannot be negative. By utilizing PuLP, the optimization model is solved efficiently, determining the best combination of Product A and Product B for maximum profitability.

After running the model, we find that the optimal solution is to produce 16 units of Product A and 12 units of Product B, which results in a maximum achievable profit of $1000. This insight allows businesses to allocate resources effectively and make data-driven decisions to enhance profitability. The project demonstrates how mathematical optimization can be applied to real-world scenarios, making it highly valuable for students, researchers, and professionals in fields like operations research, supply chain management, and data science.

This solution is implemented using Python, leveraging the PuLP library for linear programming and Jupyter Notebook for interactive computation. The project is structured to be easy to understand and run, making it a great learning resource for those new to optimization techniques. By following the provided code, users can modify parameters, experiment with different constraints, and extend the model to more complex scenarios. To run the project, simply install PuLP using pip install pulp, execute the Python script or Jupyter Notebook, and review the results.

In summary, this project provides a practical approach to solving optimization problems using linear programming. By applying mathematical models, businesses can enhance decision-making, optimize production, and increase profitability. Whether you are a student learning about optimization or a business professional looking to improve efficiency, this project serves as an excellent reference. It highlights the power of data-driven decision-making and demonstrates how computational techniques can be used to solve real-world business challenges.

OUTPUT

![image](https://github.com/user-attachments/assets/72b5338d-47a4-467c-85f9-325add7c8c30)

