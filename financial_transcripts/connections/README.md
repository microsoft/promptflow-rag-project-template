# Connections for Promptflow

In order for promptflow to safely authenticate with your tools and resources, we use [promtpflow connections](https://microsoft.github.io/promptflow/concepts/concept-connections.html). Specifically we use custom connections and suggest you specify the parameters in your `.env`. Please take the `.env.sample` and populate it with your specific resource information. Depending on the resource you need to authenticate in your flows, run the respective `connect_<resource>.py`.

For example, if you are bring your Azure OpenAI keys

```cmd
python connect_aoai.py
```


In the `.env`, specify where to get the resource information from either from the `.env` itself or a keyvault
```bash
# Use .env or keyvault. ENV or empty = .env, KEYVAULT = keyvault
KEYS_FROM="ENV"
KEY_VAULT_NAME=""
```

Be sure to be consistent with the variable names in `connect_<resource>.py` files like `OPENAI_API_KEY` and in the `.env`

> NOTE: Our convention is that variables from keyvault have a (-), but from a `.env` has a (_) like `OPENAI-API-BASE` vs. `OPENAI_API_BASE`