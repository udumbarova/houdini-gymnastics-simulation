"""
Filename: muscle_setup.py
Description: This script sets up the muscle system for the character in Houdini.
"""

import hou

def setup_muscles():
    # Create Vellum muscle system
    geo_node = hou.node('/obj/character_geo')
    muscle_system = geo_node.createNode('vellumconfigure', 'muscle_system')
    muscle_system.setInput(0, geo_node.node('character_bones'))

    # Configure muscles
    muscle_system.parm('enablepins').set(1)
    muscle_system.parm('bendstiffness').set(0.5)
    muscle_system.parm('stretchstiffness').set(0.8)

    return muscle_system

# Example usage
setup_muscles()
