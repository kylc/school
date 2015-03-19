RIB=planet.rib
SHADERS=planet_surf.sl planet_disp.sl glow.sl stars.sl atmosphere.sl clouds.sl
SHADER_OBJS=$(subst .sl,.sdl,$(SHADERS))

%.sdl: %.sl
	shaderdl $<

render: $(RIB) $(SHADER_OBJS)
	renderdl $<
	feh planet.tiff

clean:
	rm *.sdl
