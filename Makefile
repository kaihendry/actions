accounts.json: accounts.py
	uv run accounts.py > accounts.json

clean:
	rm -f accounts.json
