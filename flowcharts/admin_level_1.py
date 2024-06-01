from graphviz import Digraph
import graphviz

dot = Digraph()

dot = graphviz.Digraph(comment='User Management Process')

# Start node
dot.node('Start', 'Start', shape='ellipse')

# Process nodes
dot.node('P1', 'Login to Admin Dashboard', shape='box')
dot.node('P2', 'Navigate to User Management', shape='box')
dot.node('P3', 'Select Action', shape='diamond')

# Actions
dot.node('A1', 'Add User', shape='box')
dot.node('A2', 'Edit User', shape='box')
dot.node('A3', 'Delete User', shape='box')
dot.node('A4', 'View Users', shape='box')

# Sub-processes for Add User
dot.node('SU1', 'Enter User Details', shape='box')
dot.node('SU2', 'Submit', shape='box')

# Sub-processes for Edit User
dot.node('SE1', 'Select User', shape='box')
dot.node('SE2', 'Update Details', shape='box')
dot.node('SE3', 'Submit Changes', shape='box')

# Sub-process for Delete User
dot.node('SD1', 'Select User', shape='box')
dot.node('SD2', 'Confirm Deletion', shape='box')

# Sub-process for View Users
dot.node('SV1', 'Display User List', shape='box')

# End node
dot.node('End', 'End', shape='ellipse')

# Edges
dot.edges(['Start->P1', 'P1->P2', 'P2->P3'])
dot.edge('P3', 'A1', label='Add User')
dot.edge('P3', 'A2', label='Edit User')
dot.edge('P3', 'A3', label='Delete User')
dot.edge('P3', 'A4', label='View Users')

dot.edges(['A1->SU1', 'SU1->SU2', 'SU2->P3'])
dot.edges(['A2->SE1', 'SE1->SE2', 'SE2->SE3', 'SE3->P3'])
dot.edges(['A3->SD1', 'SD1->SD2', 'SD2->P3'])
dot.edges(['A4->SV1', 'SV1->P3'])

dot.edge('P3', 'End', label='Exit')

# Render the graph
dot.render('user_management_flowchart', format='png', cleanup=False)
