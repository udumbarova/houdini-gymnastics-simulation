"""
Filename: gymnastics_simulation.py
Description: This script creates a skeletal-muscular simulation of a character
performing the gymnastic element 'horizontal' in Houdini. It utilizes Houdini's Python API
and VEX for procedural animation and simulation, as well as Vellum for realistic muscle
modeling and balance control through Inverse Kinematics (IK).
"""

import hou

# Create a new scene
hou.hipFile.clear(suppress_save_prompt=True)

# Create a geometry object for the character
geo_node = hou.node('/obj').createNode('geo', 'character_geo')

# Create the bone network
bones = geo_node.createNode('bones', 'character_bones')
bones.setDisplayFlag(False)

# Create bones for the upper body
spine_root = bones.createNode('bone', 'spine_root')
spine_root.parm('length').set(0.5)

spine_mid = spine_root.createOutputNode('bone', 'spine_mid')
spine_mid.parm('length').set(0.5)

spine_top = spine_mid.createOutputNode('bone', 'spine_top')
spine_top.parm('length').set(0.5)

# Create bones for the arms
shoulder_left = spine_top.createOutputNode('bone', 'shoulder_left')
shoulder_left.parm('length').set(0.3)

upper_arm_left = shoulder_left.createOutputNode('bone', 'upper_arm_left')
upper_arm_left.parm('length').set(0.4)

forearm_left = upper_arm_left.createOutputNode('bone', 'forearm_left')
forearm_left.parm('length').set(0.4)

hand_left = forearm_left.createOutputNode('bone', 'hand_left')
hand_left.parm('length').set(0.2)

shoulder_right = spine_top.createOutputNode('bone', 'shoulder_right')
shoulder_right.parm('length').set(0.3)

upper_arm_right = shoulder_right.createOutputNode('bone', 'upper_arm_right')
upper_arm_right.parm('length').set(0.4)

forearm_right = upper_arm_right.createOutputNode('bone', 'forearm_right')
forearm_right.parm('length').set(0.4)

hand_right = forearm_right.createOutputNode('bone', 'hand_right')
hand_right.parm('length').set(0.2)

# Create bones for the legs
pelvis = spine_root.createOutputNode('bone', 'pelvis')
pelvis.parm('length').set(0.5)

thigh_left = pelvis.createOutputNode('bone', 'thigh_left')
thigh_left.parm('length').set(0.5)

shin_left = thigh_left.createOutputNode('bone', 'shin_left')
shin_left.parm('length').set(0.5)

foot_left = shin_left.createOutputNode('bone', 'foot_left')
foot_left.parm('length').set(0.3)

thigh_right = pelvis.createOutputNode('bone', 'thigh_right')
thigh_right.parm('length').set(0.5)

shin_right = thigh_right.createOutputNode('bone', 'shin_right')
shin_right.parm('length').set(0.5)

foot_right = shin_right.createOutputNode('bone', 'foot_right')
foot_right.parm('length').set(0.3)

# Create Vellum muscle system
muscle_system = geo_node.createNode('vellumconfigure', 'muscle_system')
muscle_system.setInput(0, geo_node.node('character_bones'))

# Configure muscles
muscle_system.parm('enablepins').set(1)
muscle_system.parm('bendstiffness').set(0.5)
muscle_system.parm('stretchstiffness').set(0.8)

# Create constraints for balance
constraints = geo_node.createNode('null', 'constraints')
constraints.setInput(0, muscle_system)

# Setup IK for balance control
ik_node = geo_node.createNode('inversekin', 'ik_balance')
ik_node.setInput(0, constraints)
ik_node.parm('solver').set('IKS')

# Animation control
null = geo_node.createNode('null', 'animation_control')
null.setDisplayFlag(True)

# Animate the horizontal element
time = hou.time()

# Spine animation
spine_top.parm('rx').setExpression('sin($T * 180)', hou.exprLanguage.Hscript)

# Arm animation
upper_arm_left.parm('rx').setExpression('cos($T * 180)', hou.exprLanguage.Hscript)
forearm_left.parm('rx').setExpression('sin($T * 180)', hou.exprLanguage.Hscript)

upper_arm_right.parm('rx').setExpression('cos($T * 180)', hou.exprLanguage.Hscript)
forearm_right.parm('rx').setExpression('sin($T * 180)', hou.exprLanguage.Hscript)

# Leg animation
thigh_left.parm('rx').setExpression('sin($T * 180)', hou.exprLanguage.Hscript)
shin_left.parm('rx').setExpression('cos($T * 180)', hou.exprLanguage.Hscript)

thigh_right.parm('rx').setExpression('sin($T * 180)', hou.exprLanguage.Hscript)
shin_right.parm('rx').setExpression('cos($T * 180)', hou.exprLanguage.Hscript)

# Set initial time and start playback
hou.setTime(0)
hou.playbar.play()
