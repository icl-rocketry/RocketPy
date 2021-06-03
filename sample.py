#tesing out the Fusion 360 API

import adsk.core, adsk.fusion, traceback


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Draw some circles.
        circles = sketch.sketchCurves.sketchCircles
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 1)

        # Add a circle at the center of one of the existing circles.
        circle3 = circles.addByCenterRadius(circle1.centerSketchPoint, 0.8)

        # Get extrude features
        extrudes = rootComp.features.extrudeFeatures

        # Get the profile defined by the circle
        prof = sketch.profiles.item(0)

        # Extrude Sample 1: A simple way of creating typical extrusions (extrusion that goes from the profile plane the specified distance).
        # Define a distance extent of 5 cm
        distance = adsk.core.ValueInput.createByReal(10)
        extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

