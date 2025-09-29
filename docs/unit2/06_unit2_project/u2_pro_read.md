#  Reading: Psuedocode

---

## Pre Class Reading Assignment

Read through the following article on pseudocode. [Pseudocode: What It Is and How to Write It](https://builtin.com/data-science/pseudocode){:target="_blank"}

!!!Note
Every programmer writes pseudocode differently. The main purpose of pseudocode is to help you plan out your code before you start writing it. It can be as simple or as detailed as you want it to be. The important thing is that it helps you understand what you need to do and how to do it.

### Another example of pseudocode

The following is an example of pseudocode for a project that is done in CE 321. Skim through it to get an idea of how pseudocode can be written and a real world example of how it can be used. In this particular example, some of the function have already been completed and the student is expected to write the code for the other functions.

```plaintext
Pseudocode for the Method of Joints function:

A line beginning with a number in parentheses indicates that this is a function. The number label is unique. The information in brackets after the function indicates input for the function. On the line immediately following the function is the name of the function in our Python code, indicated using an asterisk. Processes performed in a function are indicated by indenting them under the function. Subprocesses (e.g. things to be done in a for loop or if statement) are indicated with additional indenting. Output for a function is listed at the end of the function. 

If a process in a function is another function, it will be indicated using a number with parentheses. Pseudocode for these functions are described later in this document in the same manner as above.  

(1) Method of Joints[input CSV file]:
      *MethodOfJoints

	Load CSV data and store (2)
	Determine if the input CSV is statically determinate (3)
	Compute reaction forces at the supports from external loads (4)
	Iterate through all bars using the method of joints (5)
	
Output: Computed forces in bars

(2) Load CSV data and store[input CSV file]:
      *LoadData

	This function has already been completed for you and should not be modified.

	Output: List of nodes (including forces on nodes and supports)
		  List of bars

(3) Determine if the input CSV is statically determinate[list of nodes, list of bars]
      *StaticallyDeterminate

	This function has already been completed for you and should not be modified.

	Output: True if statically determinate, False if not

(4) Compute reaction forces at the supports from external loads[list of nodes]
      *ComputeReactions

	This function is described in another document. See the last page of this document.

	Output: Store the computed reaction forces at the nodes

(5) Iterate through all bars using the method of joints[list of nodes, list of bars]
      *IterateUsingMethodOfJoints

	Create a counter that keeps track of how many times you’ve iterated on the structure
	While any bar in the structure has not yet been computed
		If the counter is too high, assume an infinite loop and stop the code
		Loop through each of the nodes
			Determine the number of unknown bars at the node (6)
			Determine if the node is viable (7)
			If the node is viable
				If there are two unknown bars at the node
					Perform sum of the forces in the local y direction (8)
				Perform sum of the forces in the local x direction (9)
		Add one to the counter

	Output: Bars with computed internal forces

(6) Determine the number of unknown bars at the node[a single node]
      *UnknownBars

	Create an empty list of unknown bars
Loop through the list of bars at the node
		If the force in the bar is not yet known
			Store the bar in the list of unknown bars

	Output: List of bars that have internal forces that have not yet been computed
				
(7) Determine if the node is viable[list of unknown bars next to the node]
      *NodeIsViable

	If the number of unknown bars is one or two
		Output True
	Else
		Output False

	Output: True if the node is viable, False if it is not

(8) Perform sum of the forces in the local y direction[node, list of unknown bars next to node]
      *SumOfForcesInLocalY

	Define the first unknown bar next to the node as the local x bar
	Define the other unknown bar next to the nodes as the other bar
	Find the local x vector---the vector from the node in the direction of the local x bar (†)
	Determine the contribution of the external/reaction force(s) in the global y direction to 
		the force in the local y direction (†)
	Determine the contribution of the external/reaction force(s) in the global x direction to 
		the force in the local y direction (†)
	Iterate through all of the bars at the node
		If the bar is not unknown
			Include the contribution of the bar’s force in the local y direction (†)
Set the force in the other unknown bar as the sum of all of the above contributions 
divided by the sine of the CCW angle from the local x bar to the other bar,
and multiplied by -1 (†)
	Mark the other bar as known.

(9) Perform sum of the forces in the local x direction[node, list of unknown bars next to node]
      *SumOfForcesInLocalX

Define the first unknown bar next to the node as the local x bar
	Find the local x vector---the vector from the node in the direction of the local x bar (†)
	Determine the contribution of the external/reaction force(s) in the global y direction to 
		the force in the local x direction (†)
	Determine the contribution of the external/reaction force(s) in the global x direction to 
		the force in the local x direction (†)
	Iterate through all of the bars at the node
		If the bar is not unknown
			Include the contribution of the bar’s force in the local x direction (†)
Set the force in the local x bar as the sum of all of the above contributions 
multiplied by -1
	Mark the bar as known.
```

---

## Pre-Class Quiz Challenge

The Pre-Class Quiz Challenge will be found inside the Learning Suite quiz for this topic.