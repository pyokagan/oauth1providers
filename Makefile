providers_src = $(wildcard providers/*.yaml)

all: providers.json

providers.json: $(providers_src)
	./build.py $^ > $@

clean:
	rm -rf providers.json

.PHONY: all clean
