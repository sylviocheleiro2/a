import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
fig.set_facecolor('black')  # Set background color to black

# Slightly larger cranium for shading
cranium_shade = patches.Circle((0.5, 0.5), 0.41, facecolor='#333333') 
ax.add_patch(cranium_shade)

cranium = patches.Circle((0.5, 0.5), 0.4, facecolor='white', edgecolor='black')
ax.add_patch(cranium)

left_eye = patches.Circle((0.35, 0.65), 0.075, facecolor='black')
right_eye = patches.Circle((0.65, 0.65), 0.075, facecolor='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

nose = patches.Polygon([[0.5, 0.5], [0.45, 0.4], [0.55, 0.4]], closed=True, facecolor='#333333', edgecolor='black') # Darker nose
ax.add_patch(nose)

mouth = patches.Polygon([[0.3, 0.3], [0.7, 0.3]], closed=False, linewidth=2, edgecolor='black')
ax.add_patch(mouth)

hat_top = patches.Rectangle((0.2, 0.8), 0.6, 0.15, facecolor='purple')
hat_brim = patches.Rectangle((0.1, 0.75), 0.8, 0.05, facecolor='purple')
ax.add_patch(hat_top)
ax.add_patch(hat_brim)

left_fire1 = patches.Polygon([[0.3, 0.7], [0.4, 0.8], [0.35, 0.9]], closed=True, facecolor='yellow', edgecolor='orange')
left_fire2 = patches.Polygon([[0.32, 0.75], [0.38, 0.85], [0.35, 0.95]], closed=True, facecolor='red', edgecolor='yellow')
right_fire1 = patches.Polygon([[0.6, 0.7], [0.7, 0.8], [0.65, 0.9]], closed=True, facecolor='yellow', edgecolor='orange')
right_fire2 = patches.Polygon([[0.62, 0.75], [0.68, 0.85], [0.65, 0.95]], closed=True, facecolor='red', edgecolor='yellow')
ax.add_patch(left_fire1)
ax.add_patch(left_fire2)
ax.add_patch(right_fire1)
ax.add_patch(right_fire2)

mouth_left = patches.Polygon([[0.45, 0.3], [0.5, 0.25], [0.55, 0.3]], closed=True, linewidth=2, edgecolor='black', fill=False)
mouth_right = patches.Polygon([[0.55, 0.3], [0.6, 0.25], [0.65, 0.3]], closed=True, linewidth=2, edgecolor='black', fill=False)
ax.add_patch(mouth_left)
ax.add_patch(mouth_right)

ax.set_aspect('equal')
ax.autoscale_view()
plt.axis('off')
plt.show()