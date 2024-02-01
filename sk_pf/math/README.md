# Semantic Kernel Planner with Promptflow

After trying this [public sample](https://github.com/MicrosoftDocs/semantic-kernel-docs/tree/main/samples/python/12-Evaluate-with-Prompt-Flow), it was found the sdk was updated and it no longer works. The purpose of this sample is to demonstrate it working in our existing workflow.

## Steps

1. cd `sk_pf/`
2. Open the `flow.dag.yaml`
3. Ensure you have created connections for aoai. In the `flow.dag.yaml`, update modelConnections.
4. Hit run!

## Extending this sample

The plugins are native functions in the `plugins/` folder. They are a class that you specify a semantic kernel decorator for. We add the plugins to the kernel for the planner to decide from all the plugins with a "description" in the decorator.

```
math_plugin = kernel.import_plugin(Math(), "MathPlugin")
```