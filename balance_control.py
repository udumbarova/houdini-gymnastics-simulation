"""
Filename: balance_control.py
Description: This script sets up the balance control using Inverse Kinematics (IK) in Houdini.
"""

import hou

def setup_balance():
    geo_node = hou.node('/obj/character_geo')
    constraints = geo_node.createNode('null', 'constraints')
    constraints.setInput(0, geo_node.node('muscle_system'))

    # Setup IK for balance control
    ik_node = geo_node.createNode('inversekin', 'ik_balance')
    ik_node.setInput(0, constraints)
    ik_node.parm('solver').set('IKS')

    return ik_node

# Example usage
setup_balance()
