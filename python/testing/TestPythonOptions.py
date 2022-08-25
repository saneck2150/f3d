import f3d

engine = f3d.engine(f3d.window.NONE)

assert engine.getOptions().getAsBool("interactor.axis") is False
assert engine.getOptions().getAsDouble("model.material.roughness") == 0.3
assert engine.getOptions().getAsInt("render.raytracing.samples") == 5
assert engine.getOptions().getAsDoubleVector("model.color.rgb") == [ 1., 1., 1.]
assert engine.getOptions().getAsString("scene.up-direction") == "+Y"

options = f3d.options()
options.set("interactor.axis", True)
options.set("model.material.roughness", 0.7)
options.set("render.raytracing.samples", 2)
options.set("model.color.rgb", [ 0., 1., 1.])
options.set("scene.up-direction", "-Z")

engine.setOptions(options)

assert engine.getOptions().getAsBool("interactor.axis") is True
assert engine.getOptions().getAsDouble("model.material.roughness") == 0.7
assert engine.getOptions().getAsInt("render.raytracing.samples") == 2
assert engine.getOptions().getAsDoubleVector("model.color.rgb") == [ 0., 1., 1.]
assert engine.getOptions().getAsString("scene.up-direction") == "-Z"