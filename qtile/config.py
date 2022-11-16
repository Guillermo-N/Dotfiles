### QTile windows manager configuration ###

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    
    # MOD + FUNCTION KEY
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # MOD + SHIFT KEYS
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "r", lazy.restart()),
    

    # MOD + CONTROL KEYS
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),j
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


def init_layout_theme():
    return {"margin": 1,
            "border_witdth": 2,
            "border_focus": '#1298ba',
            "border_normal": '#665f54'
            }


def init_colors():
    color_set1 = [['#4a4a46', '#4a4a46'],
                  ['#121417', '#665f54'], # color 0 
                  ['#c94134', '#ff645a'], # color 1
                  ['#85c54c', '#98e036'], # color 2
                  ['#f5ae2d', '#dfd562'], # color 3
                  ['#1298ba', '#5edaff'], # color 4
                  ['#d0623c', '#ff9268'], # color 5
                  ['#509452', '#8efc93'], # color 6 #'#83f088'
                  ['#e5c5aa', '#f6f6ec']] # color 7

    color_set2 = [['#121417', '#121417'], # color 0 
                  ['#c94134', '#c94134'], # color 1
                  ['#85c54c', '#85c54c'], # color 2
                  ['#f5ae2d', '#f5ae2d'], # color 3
                  ['#1298ba', '#1298ba'], # color 4
                  ['#d0623c', '#d0623c'], # color 5
                  ['#509452', '#509452'], # color 6 
                  ['#e5c5aa', '#e5c5aa'], # color 7
                  ['#665f54', '#665f54']] # color 8
                  
    return color_set2

colors = init_colors()
layout_theme = init_layout_theme()

layouts = [
    #layout.Columns(border_focus_stack=colors[7], border_width=2),
    layout.RatioTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=18,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    foreground = colors[6],
                    background = colors[0]
                ),
                widget.GroupBox(
                    #highlight_method = 'line',
                    disable_drag = True,
                    borderwidth = 2,
                    padding_y = 1,
                    padding_x = 2,
                    margin_y = 3,
                    margin_x = 4,
                    active = colors[3],
                    inactive = colors[8],
                    highlight_color= colors[3],
                    this_current_screen_border= colors[6],
                    foreground = colors[7],
                    background = colors[0]
                ),
                widget.Prompt(),
                widget.Spacer(),
                widget.Backlight(
                    fmt='💡{}',
                    change_command='brigthtnessctl set {0}',
                    brightness_file='/sys/class/backlight/amdgpu_bl0/brightness',
                    max_brightness_file='/sys/class/backlight/amdgpu_bl0/max_brightness',
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Memory(
                    measure_mem='G',
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.DF(
                    measure='G',
                    warn_space=20,
                    visible_on_warn=False,
                    partition='/',
                    format='{r:.0f}%',
                    fmt='💾{}',
                    foreground = colors[7]
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Load(
                    format='🧮{load:.1f}',
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.ThermalZone(
                    high=45, 
                    crit=50,
                    fmt='🌡️{}',
                    fgcolor_normal = colors[7],
                    fgcolor_high = colors[3],
                    fgcolor_crit = colors[1]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Battery(
                    charge_char="🔌",
                    empty_char="🪫",
                    discharge_char="🔋",
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Volume(
                    emoji=True,
                    device = 'default',
                    scroll = True,
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                #widget.Wlan(interface='wlp3s0', format='{essid} {percent:2.0%}'),
                widget.Net(
                    prefix='M', 
                    interface='wlp3s0',
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Bluetooth(),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Wttr(
                    location={'Brno': 'Brno'},
                    foreground = colors[7],
                    fmt = '{}',
                    format = 2
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Clock(
                    format="%I:%M %p // %d-%m-%Y",
                    foreground = colors[7]
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 8,
                    foreground = colors[4],
                    background = colors[0]
                ),
                widget.Systray(),
                widget.Wallpaper(
                    directory = '~/Pictures/wallpapers/',
                    wallpaper_command = ['feh', '--bg-fill'],
                    random_selection = True,
                    fmt = '🧭'
                ),
                #widget.QuickExit(),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
