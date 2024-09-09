"""
Small Horus block to set all remotes on the current flow to the same value.
"""

from HorusAPI import Plugin, PluginBlock, PluginVariable, VariableTypes

any_input_output_variable = PluginVariable(
    id="any_input_output_variable",
    name="Any variable",
    description="Variable that contains any input or output. Use it to concatenate this block with other blocks.",
    type=VariableTypes.ANY,  # type: ignore
)


def set_all_remotes_action(block: PluginBlock):
    """Set all remotes on the current flow to the same value."""

    print(f"Setting all remotes to '{block.selectedRemote}'")

    for b in block.flow.blocks:
        b.selectedRemote = block.selectedRemote

    block.setOutput(
        any_input_output_variable.id, block.inputs[any_input_output_variable.id]
    )


set_all_remotes_block = PluginBlock(
    id="set_all_remotes",
    name="Set All Remotes",
    description="Set all remotes on the current flow to the same value.",
    action=set_all_remotes_action,
    inputs=[any_input_output_variable],
    outputs=[any_input_output_variable],
)

plugin = Plugin()
plugin.addBlock(set_all_remotes_block)
