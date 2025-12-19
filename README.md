# Components Library for Python/FastHTML

A Python component library following atomic design principles for FastHTML applications.

## Installation

```bash
pip install components-library
# or with uv
uv add components-library
```

For development:
```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from fasthtml.common import serve
from components_library import base_page, card, heading, button, vstack

def home():
    return base_page(
        card(
            vstack(
                heading("Welcome to Labs App", level=1),
                button("Get Started", variant="solid", color_palette="brand"),
                gap=4
            )
        ),
        title="Labs App"
    )

serve()
```

## Architecture

This library follows **atomic design principles**:

```
components_library/
├── design_system/         # Design tokens and theme
│   ├── tokens/           # Colors, spacing, typography, etc.
│   └── theme/            # Base styles and component styles
├── utils/                # Helper functions
│   ├── component_helpers.py
│   ├── htmx_helpers.py
│   └── style_generator.py
└── components/           # UI Components
    ├── atoms/            # Basic building blocks
    ├── molecules/        # Combinations of atoms
    ├── organisms/        # Complex components
    └── templates/        # Page layouts
```

## Components

### Atoms (Basic Building Blocks)

Layout:
- `box` - Generic container with styling
- `flex` - Flexbox layout container
- `grid` - Grid layout container
- `vstack`, `hstack` - Vertical/horizontal stacks
- `separator` - Divider line

Typography:
- `text` - Styled text with variants (body, caption, label, helper, error)
- `heading` - Headings h1-h6 with consistent sizing

Inputs:
- `input` - Text input with types and states
- `select` - Dropdown select
- `checkbox`, `radio` - Selection inputs
- `textarea` - Multi-line text input
- `switch` - Toggle switch
- `slider` - Range slider
- `date_input` - Date picker input

Buttons:
- `button` - Primary interaction element with variants
- `icon_button` - Icon-only button
- `button_link` - Link styled as button

Feedback:
- `alert` - Alert messages (info, success, warning, error)
- `badge` - Status badges
- `tag` - Tags with optional close button
- `spinner` - Loading spinner
- `progress` - Progress bar
- `skeleton` - Loading skeleton

Containers:
- `card` - Card container
- `modal` - Modal dialog
- `popover` - Popover overlay
- `tooltip` - Tooltip hints
- `accordion`, `accordion_item` - Collapsible sections
- `collapsible` - Collapsible container
- `tabs`, `tab_panel` - Tabbed interface

Navigation:
- `menu`, `menu_item`, `menu_divider` - Dropdown menu
- `pagination` - Pagination controls
- `link` - Styled anchor link

Other:
- `avatar` - User avatar with initials/image
- `icon` - Icon renderer
- `logo` - Logo display
- `empty_state` - Empty state UI
- `field` - Form field wrapper with label and error handling

### Molecules (Composed Components)

- `auth_form` - Login/signup form
- `search_bar`, `enhanced_search_bar` - Search inputs
- `filter_panel`, `filter_bar` - Filtering UI
- `file_dropzone`, `file_upload_progress` - File upload
- `breadcrumbs` - Navigation breadcrumbs
- `tag_manager` - Tag management with add/remove
- `loading_screen` - Full-page loading overlay
- And more...

### Organisms (Complex Components)

- `navigation` - Responsive navigation with mobile menu
- `data_table` - Table with search, filters, pagination
- `page_header` - Page header component
- `alphabet_browser` - Alphabetical content browser

### Templates (Page Layouts)

- `base_page` - HTML page template with styles and HTMX
- `auth_page_layout` - Centered auth page layout
- `centered_content` - Centered content container

## Design System

### Using Design Tokens

```python
from components_library import Colors, Spacing, Typography

colors = Colors()
spacing = Spacing()
typography = Typography()

# Access color values
primary_color = colors.primary.s600  # "#2563eb"
text_color = colors.text_primary     # "#171717"

# Access spacing values
padding = spacing._4  # "1rem"

# Access typography
font_size = typography.base.size  # "1rem"
```

### Available Tokens

**Colors:**
- `primary` - Blue primary palette (50-950)
- `neutral` - Gray neutral palette
- `success` - Green success palette
- `warning` - Yellow/orange warning palette
- `error` - Red error palette
- Semantic: `text_primary`, `text_secondary`, `text_disabled`, `background`, `background_alt`, `border`, `border_focus`

**Spacing:** 0-96 scale based on 4px increments

**Typography:**
- Font sizes: xs, sm, base, lg, xl, xl2-xl9
- Font weights: thin to black

**Effects:**
- Shadows: xs, sm, md, lg, xl, xl2
- Border radius: none, sm, base, md, lg, xl, xl2, xl3, full
- Transitions: fast, base, slow, slower

## HTMX Integration

Components have built-in HTMX support:

```python
from components_library import button, input

# Button with HTMX
button(
    "Delete",
    hx_delete="/api/item/1",
    hx_confirm="Are you sure?",
    hx_swap="outerHTML",
    color_palette="red"
)

# Input with debounced search
input(
    name="search",
    hx_get="/api/search",
    hx_trigger="keyup changed delay:300ms",
    hx_target="#results"
)
```

HTMX helper utilities:

```python
from components_library import htmx_attrs, debounced_search, confirm_delete

# Generate HTMX attributes
attrs = htmx_attrs(get="/api/data", target="#results", swap="innerHTML")

# Debounced search pattern
attrs = debounced_search("/api/search", "#results", delay=300)

# Confirm delete pattern
attrs = confirm_delete("/api/item/1", "Are you sure?")
```

## Styling

Components use CSS classes that are generated by the theme. Include styles in your page:

```python
from components_library import base_page

# base_page automatically includes all styles
page = base_page(content, title="Labs App")
```

Or include styles manually:

```python
from components_library import base_styles, component_styles, htmx_script

# In your HTML head
styles = f"<style>{base_styles()}</style><style>{component_styles()}</style>"
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run linting
ruff check .

# Run type checking
mypy components_library/

# Run tests
pytest
```

## License

Proprietary
