"""Comprehensive UI showcase page demonstrating all components."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...design_system import get_theme_css
from ..atoms import (
    accordion,
    accordion_item,
    alert,
    autocomplete_input,
    avatar,
    badge,
    box,
    button,
    button_link,
    card,
    checkbox,
    chip_select,
    collapsible,
    confidence_score,
    date_input,
    editable_heading,
    empty_state,
    field,
    flex,
    grid,
    heading,
    hstack,
    icon,
    icon_button,
    input,
    link,
    logical_operator,
    logo,
    menu,
    menu_divider,
    menu_item,
    modal,
    pagination,
    popover,
    progress,
    radio,
    responsive_text,
    select,
    separator,
    skeleton,
    slider,
    spinner,
    switch,
    tab_panel,
    table,
    tabs,
    tag,
    text,
    textarea,
    tooltip,
    voice_waveform,
    vstack,
)
from ..molecules import (
    BackgroundJob,
    BreadcrumbItem,
    ChildEntry,
    FilterGroup,
    TagItem,
    Token,
    UserAction,
    action_card,
    auth_form,
    breadcrumbs,
    carousel,
    child_entries_section,
    completion_circle,
    dashboard_nav_card,
    dashboard_stat_card,
    date_range_inputs,
    detail_row,
    details_section,
    discrete_slider,
    editable_header,
    enhanced_search_bar,
    entity_card,
    error_fallback,
    favorite_button,
    file_dropzone,
    file_upload_progress,
    filter_bar,
    filter_panel,
    footer,
    form_card_select,
    form_modal,
    hero_card,
    htmx_file_dropzone,
    htmx_pagination,
    htmx_tag_manager,
    icon_card,
    image_uploader,
    item_details,
    job_status_banner,
    loading_screen,
    nav_card,
    overflow_tooltip,
    removable_entity_row,
    result_card,
    scene_card,
    search_bar,
    search_results,
    stat_card,
    stats_chart,
    tab_state_wrapper,
    tag_manager,
    timeline_card,
    timeline_event_card,
    timeline_lane,
    token_pill,
    user_actions,
    user_nav,
)
from ..organisms import (
    NotificationItem,
    SearchToken,
    alphabet_browser,
    articles_search,
    data_table,
    feature_card,
    header,
    hero_section,
    kanban_board,
    kanban_column,
    navigation,
    notifications,
    page_header,
    profile_card,
    relationship_board,
    timeline_view,
)
from .auth_page_layout import auth_page_layout
from .base_page import base_page
from .centered_content import centered_content
from .error_template import error_template
from .labs_intro_page import BadgeConfig, labs_intro_page
from .page_container import page_container
from .sidebar_layout import sidebar_layout


def _showcase_card(component_name: str, *content: Any, **kwargs: Any) -> Div:
    """Wrap a component example in a card for clear visual separation."""
    return card(
        vstack(
            heading(
                component_name,
                level=4,
                style="color: var(--color-primary-600); margin-bottom: 0.75rem;",
            ),
            *content,
            gap=2,
        ),
        style="padding: 1.5rem; margin-bottom: 1rem; border: 1px solid var(--color-border-default); background: var(--color-background);",
        **kwargs,
    )


def _atoms_showcase() -> Any:
    """Atoms Section."""
    return collapsible(
        heading("Atoms", level=2, style="color: var(--color-primary-600);"),
        vstack(
            # Buttons
            vstack(
                heading("Buttons", level=3, size="lg", style="color: var(--color-primary-500);"),
                _showcase_card(
                    "Button Colors",
                    hstack(
                        button("Brand", color_palette="brand"),
                        button("Gray", color_palette="gray"),
                        button("Red", color_palette="red"),
                        button("Green", color_palette="green"),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Button Sizes",
                    hstack(
                        button("XS", size="xs"),
                        button("SM", size="sm"),
                        button("MD", size="md"),
                        button("LG", size="lg"),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Button Variants",
                    hstack(
                        button("Primary", variant="solid"),
                        button("Secondary", variant="outline"),
                        button("Ghost", variant="ghost"),
                        icon_button("⚙️", aria_label="Settings"),
                        link("Link", href="#"),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Logical Operator",
                    hstack(
                        logical_operator("AND"),
                        logical_operator("OR"),
                        logical_operator("AND NOT"),
                        gap=2,
                    ),
                ),
                gap=3,
            ),
            separator(),
            # Data Display
            vstack(
                heading(
                    "Data Display", level=3, size="lg", style="color: var(--color-primary-500);"
                ),
                _showcase_card(
                    "Card",
                    card(
                        text("Card content"),
                        header=heading("Card Title", level=4),
                        footer=hstack(
                            button("Cancel", variant="outline", size="sm"),
                            button("Save", size="sm"),
                            gap=2,
                        ),
                    ),
                ),
                _showcase_card(
                    "Empty State",
                    empty_state(
                        "No items found",
                        title="Get Started",
                        icon="📭",
                        action=button("Add Item", variant="outline", size="sm"),
                    ),
                ),
                _showcase_card(
                    "Pagination",
                    pagination(current_page=2, total_pages=5),
                ),
                _showcase_card(
                    "Table",
                    table(
                        headers=["Name", "Status", "Score"],
                        rows=[
                            ["Alice", badge("Active", variant="success"), "95%"],
                            ["Bob", badge("Pending", variant="gray"), "82%"],
                            ["Carol", badge("Error", variant="error"), "N/A"],
                        ],
                        striped=True,
                    ),
                ),
                _showcase_card(
                    "Voice Waveform",
                    voice_waveform(
                        height="40px",
                        primary_color="var(--color-primary-500)",
                        secondary_color="var(--color-secondary-500)",
                    ),
                ),
                gap=3,
            ),
            separator(),
            # Feedback
            vstack(
                heading("Feedback", level=3, size="lg", style="color: var(--color-primary-500);"),
                _showcase_card(
                    "Alert Variants",
                    vstack(
                        alert("Informational message", variant="info"),
                        alert("Success message", variant="success"),
                        alert("Warning message", variant="warning"),
                        alert("Error message", variant="error"),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Avatar",
                    hstack(
                        avatar(name="AB", size=32),
                        avatar(name="CD", size=40),
                        avatar(name="EF", size=48),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Badge & Tag",
                    hstack(
                        badge("New"),
                        badge("Active", variant="success"),
                        badge("Neutral", variant="gray"),
                        badge("Error", variant="error"),
                        tag("Python"),
                        tag("FastHTML"),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Confidence Score",
                    vstack(
                        hstack(text("Low (30%):"), confidence_score(30), gap=2),
                        hstack(text("Medium (60%):"), confidence_score(60), gap=2),
                        hstack(text("High (90%):"), confidence_score(90), gap=2),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Progress",
                    vstack(
                        progress(25, show_label=True),
                        progress(50, show_label=True),
                        progress(75, show_label=True),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Skeleton",
                    vstack(
                        skeleton(variant="text", width="80%"),
                        skeleton(variant="text", width="60%"),
                        skeleton(variant="circular", width="3rem", height="3rem"),
                        skeleton(variant="rectangular", width="100%", height="8rem"),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Spinner",
                    hstack(spinner(size="sm"), spinner(size="md"), spinner(size="lg"), gap=3),
                ),
                gap=3,
            ),
            separator(),
            # Forms
            vstack(
                heading("Forms", level=3, size="lg", style="color: var(--color-primary-500);"),
                _showcase_card(
                    "Checkbox, Radio & Switch",
                    hstack(
                        checkbox(name="terms", label="I agree to terms"),
                        switch(name="notifications", label="Notifications"),
                        gap=4,
                    ),
                    vstack(
                        text("Choose size:", style="font-weight: 500;"),
                        radio(name="size", value="sm", label="Small"),
                        radio(name="size", value="md", label="Medium", checked=True),
                        radio(name="size", value="lg", label="Large"),
                        gap=2,
                        style="align-items: flex-start;",
                    ),
                ),
                _showcase_card(
                    "Chip Select (Multi-select)",
                    vstack(
                        text("Select tones:", style="font-weight: 500;"),
                        chip_select(
                            name="tones",
                            options=["Dark", "Hopeful", "Gritty", "Mysterious", "Action-Packed"],
                            selected=["Dark", "Gritty"],
                        ),
                        separator(),
                        text("Select categories:", style="font-weight: 500;"),
                        chip_select(
                            name="categories",
                            options=[
                                ("sci_fi", "Sci-Fi"),
                                ("fantasy", "Fantasy"),
                                ("horror", "Horror"),
                            ],
                            selected=["fantasy"],
                            size="sm",
                        ),
                        gap=3,
                    ),
                ),
                _showcase_card(
                    "Date & Autocomplete",
                    hstack(
                        field(
                            date_input(name="start_date", value="2024-01-01"),
                            label="Start Date",
                        ),
                        field(
                            autocomplete_input(
                                name="search",
                                placeholder="Type to search...",
                                search_url="/api/search",
                            ),
                            label="Search",
                        ),
                        gap=3,
                        style="flex-wrap: wrap;",
                    ),
                ),
                _showcase_card(
                    "Input & Textarea",
                    hstack(
                        field(input(name="email", placeholder="Email"), label="Email"),
                        field(
                            select(name="role", options=[("", "Select"), ("admin", "Admin")]),
                            label="Role",
                        ),
                        gap=3,
                        style="flex-wrap: wrap;",
                    ),
                    field(
                        textarea(name="description", placeholder="Enter description", rows=3),
                        label="Description",
                    ),
                ),
                _showcase_card(
                    "Slider",
                    slider(name="volume", value=75, label="Volume", show_value=True),
                ),
                gap=3,
            ),
            separator(),
            # Icons & Logo
            vstack(
                heading(
                    "Icons & Logo", level=3, size="lg", style="color: var(--color-primary-500);"
                ),
                _showcase_card(
                    "Icons",
                    hstack(
                        icon("🏠", size="sm"),
                        icon("⚙️", size="md"),
                        icon("❤️", size="lg", color="red"),
                        icon("⭐", size="lg", color="gold"),
                        gap=3,
                    ),
                ),
                _showcase_card(
                    "Logo",
                    hstack(
                        logo(text="MyApp", size="sm"),
                        logo(text="MyApp", size="md"),
                        logo(text="MyApp", size="lg"),
                        gap=3,
                    ),
                ),
                gap=3,
            ),
            separator(),
            # Interactive
            vstack(
                heading(
                    "Interactive", level=3, size="lg", style="color: var(--color-primary-500);"
                ),
                _showcase_card(
                    "Accordion",
                    accordion(
                        accordion_item(
                            "What is this library?", text("A FastHTML component library"), open=True
                        ),
                        accordion_item("How to use?", text("Import and use components")),
                    ),
                ),
                _showcase_card(
                    "Collapsible",
                    collapsible(
                        text("Click to expand"),
                        text("This is the hidden content that appears when expanded."),
                        open=False,
                    ),
                ),
                _showcase_card(
                    "Tabs",
                    tabs(
                        ["Overview", "Details", "Settings"],
                        tab_panel(text("Overview content"), panel_index=0),
                        tab_panel(text("Details content"), panel_index=1),
                        tab_panel(text("Settings content"), panel_index=2),
                    ),
                ),
                gap=3,
            ),
            separator(),
            # Layout
            vstack(
                heading("Layout", level=3, size="lg", style="color: var(--color-primary-500);"),
                _showcase_card(
                    "Flex Layout",
                    flex(
                        box("Item 1", padding="1rem", background="var(--color-blue-100)"),
                        box("Item 2", padding="1rem", background="var(--color-blue-200)"),
                        box("Item 3", padding="1rem", background="var(--color-blue-300)"),
                        gap="0.5rem",
                    ),
                ),
                _showcase_card(
                    "Grid Layout",
                    grid(
                        box("Grid 1", padding="1rem", background="var(--color-green-100)"),
                        box("Grid 2", padding="1rem", background="var(--color-green-200)"),
                        box("Grid 3", padding="1rem", background="var(--color-green-300)"),
                        box("Grid 4", padding="1rem", background="var(--color-green-100)"),
                        columns=2,
                        gap="0.5rem",
                    ),
                ),
                _showcase_card(
                    "HStack & VStack",
                    vstack(
                        text("HStack (horizontal):"),
                        hstack(
                            badge("One"),
                            badge("Two"),
                            badge("Three"),
                            gap=2,
                        ),
                        text("VStack (vertical):"),
                        vstack(
                            badge("First"),
                            badge("Second"),
                            badge("Third"),
                            gap=1,
                        ),
                        gap=3,
                    ),
                ),
                gap=3,
            ),
            separator(),
            # Overlays & Menus
            vstack(
                heading(
                    "Overlays & Menus", level=3, size="lg", style="color: var(--color-primary-500);"
                ),
                _showcase_card(
                    "Menu",
                    menu(
                        button("Actions", variant="outline"),
                        menu_item("Edit", icon="✏️", href="#edit"),
                        menu_item("Duplicate", icon="📋", href="#duplicate"),
                        menu_divider(),
                        menu_item("Delete", icon="🗑️", href="#delete"),
                    ),
                ),
                _showcase_card(
                    "Modal",
                    vstack(
                        modal(
                            text("Are you sure you want to proceed?"),
                            modal_id="showcase-modal",
                            title="Confirm Action",
                            footer=hstack(
                                button("Cancel", variant="outline", size="sm"),
                                button("Confirm", size="sm"),
                                gap=2,
                            ),
                        ),
                        text(
                            "(Use showModal() to open - native dialog element)",
                            variant="caption",
                        ),
                        gap=2,
                    ),
                ),
                _showcase_card(
                    "Popover",
                    popover(
                        button("Click for info", variant="outline"),
                        heading("Popover Title", level=4),
                        text("This is popover content with more details"),
                        position="bottom",
                    ),
                ),
                _showcase_card(
                    "Tooltip",
                    hstack(
                        tooltip(button("Hover me", variant="outline"), "This is helpful info"),
                        tooltip(icon("ℹ️"), "Information tooltip", position="right"),
                        gap=3,
                    ),
                ),
                gap=3,
            ),
            separator(),
            # Typography
            vstack(
                heading("Typography", level=3, size="lg", style="color: var(--color-primary-500);"),
                _showcase_card(
                    "Heading Levels",
                    heading("H1 Heading", level=1),
                    heading("H2 Heading", level=2),
                    heading("H3 Heading", level=3),
                    text("Body text"),
                    text("Caption text", variant="caption"),
                ),
                _showcase_card(
                    "Responsive Text",
                    responsive_text(
                        "This text adapts to screen size",
                        size_mobile="sm",
                        size_tablet="lg",
                        size_desktop="xl2",
                        weight="semibold",
                    ),
                ),
                gap=3,
            ),
            gap=5,
        ),
        open=True,
    )


def _molecules_showcase() -> Any:
    """Molecules Section."""
    return collapsible(
        heading("Molecules", level=2, style="color: var(--color-primary-600);"),
        vstack(
            _showcase_card(
                "Action Card",
                action_card(
                    "Quick Action",
                    "Click this card to trigger an action",
                    hx_get="/example",
                ),
            ),
            _showcase_card(
                "Auth Form",
                vstack(
                    text("Login form:", variant="caption"),
                    auth_form(form_type="login", action="/login"),
                    gap=2,
                ),
            ),
            _showcase_card(
                "Breadcrumbs",
                breadcrumbs(
                    [
                        BreadcrumbItem(name="Home", href="/"),
                        BreadcrumbItem(name="Components", href="/components"),
                        BreadcrumbItem(name="Showcase"),
                    ]
                ),
            ),
            _showcase_card(
                "Carousel",
                carousel(
                    card(text("Slide 1 - First item"), style="padding: 2rem; text-align: center;"),
                    card(text("Slide 2 - Second item"), style="padding: 2rem; text-align: center;"),
                    card(text("Slide 3 - Third item"), style="padding: 2rem; text-align: center;"),
                ),
            ),
            _showcase_card(
                "Child Entries Section",
                child_entries_section(
                    entries=[
                        ChildEntry(
                            id="1", title="Subcategory A", description="First subcategory", href="#"
                        ),
                        ChildEntry(
                            id="2",
                            title="Subcategory B",
                            description="Second subcategory",
                            href="#",
                        ),
                    ],
                    title="Sub-Categories",
                    empty_message="No subcategories yet",
                ),
            ),
            _showcase_card(
                "Completion Circle",
                completion_circle("Book 1", percentage=45, subtitle="Draft Completion"),
            ),
            _showcase_card(
                "Date Range",
                date_range_inputs(start_date="2024-01-01", end_date="2024-12-31"),
            ),
            _showcase_card(
                "Detail Row",
                vstack(
                    detail_row("Item ID", "12345"),
                    detail_row("Status", "Active"),
                    detail_row("Created", "2024-01-15"),
                    separator(),
                    text("Vertical layout:", variant="caption"),
                    detail_row(
                        "Description",
                        "This is a longer text that works better in vertical layout",
                        vertical=True,
                    ),
                    gap=2,
                ),
            ),
            _showcase_card(
                "Details Section",
                details_section(
                    [
                        ("Name", "John Doe"),
                        ("Email", "john@example.com"),
                        ("Role", "Administrator"),
                        ("Status", "Active"),
                    ]
                ),
            ),
            _showcase_card(
                "Discrete Selection Slider",
                discrete_slider(
                    "demo_slider",
                    value="Main",
                    options=[("Prequel", 0), ("Main", 1), ("Sequel", 2)],
                    label="Timeline",
                ),
            ),
            _showcase_card(
                "Editable Header",
                vstack(
                    text("Read mode (click to edit):", variant="caption"),
                    editable_header(
                        value="Click Me or the Pencil",
                        name="demo-header",
                        post_url="/post/echo",
                        edit_url="/post/echo?edit=true",
                        placeholder="Enter title...",
                        level=2,
                    ),
                    separator(),
                    text("Edit mode (blur or click checkmark to save):", variant="caption"),
                    editable_header(
                        value="Currently Editing",
                        name="demo-header-edit",
                        post_url="/post/echo",
                        level=3,
                        is_editing=True,
                    ),
                    gap=3,
                ),
            ),
            _showcase_card(
                "Editable Heading",
                editable_heading(
                    value="Click to Edit Me",
                    name="demo-heading",
                    post_url="/post/echo",
                    placeholder="Enter title...",
                    level=2,
                ),
            ),
            _showcase_card(
                "Enhanced Search Bar",
                enhanced_search_bar(
                    placeholder="Enhanced search with icons...",
                    right_icon="filter",
                ),
            ),
            _showcase_card(
                "Entity Card",
                grid(
                    entity_card(
                        title="Hero Character",
                        subtitle="Protagonist",
                        image_url="https://ui-avatars.com/api/?name=Hero",
                        meta="Level 5 • 100 XP",
                        tags=["Warrior", "Leader"],
                    ),
                    entity_card(
                        title="Magic Sword",
                        subtitle="Legendary Item",
                        image_url="https://ui-avatars.com/api/?name=Sword&background=random",
                        meta="Damage: 50-100",
                        tags=["Weapon", "Rare"],
                    ),
                    columns=2,
                    gap="1rem",
                ),
            ),
            _showcase_card(
                "Error Fallback",
                error_fallback(
                    error="Failed to load data",
                    title="Something went wrong",
                    show_retry=True,
                ),
            ),
            _showcase_card(
                "Favorite Button",
                hstack(
                    favorite_button(item_id=1, is_favorite=False),
                    favorite_button(item_id=2, is_favorite=True),
                    gap=2,
                ),
            ),
            _showcase_card(
                "File Dropzone",
                file_dropzone(accept=".csv,.xlsx", accepted_formats="CSV, Excel", max_size="10MB"),
            ),
            _showcase_card(
                "File Upload Progress",
                vstack(
                    file_upload_progress(
                        file_name="data.csv",
                        file_size=1024000,
                        progress_value=65,
                        status="uploading",
                    ),
                    file_upload_progress(
                        file_name="complete.xlsx",
                        file_size=2048000,
                        progress_value=100,
                        status="complete",
                    ),
                    gap=2,
                ),
            ),
            _showcase_card(
                "Filter Bar",
                filter_bar(result_count=42),
            ),
            _showcase_card(
                "Filter Panel",
                filter_panel(
                    filters=[
                        FilterGroup(
                            id="status",
                            title="Status",
                            type="checkbox",
                            options=[("active", "Active", False), ("pending", "Pending", False)],
                            value=["active"],
                        ),
                        FilterGroup(
                            id="priority",
                            title="Priority",
                            type="radio",
                            options=[
                                ("low", "Low", False),
                                ("medium", "Medium", False),
                                ("high", "High", False),
                            ],
                            value="medium",
                        ),
                    ],
                    on_filter_change=lambda _f, _v: None,
                    variant="inline",
                ),
            ),
            _showcase_card(
                "Footer",
                footer(),
            ),
            _showcase_card(
                "Form Card Select",
                form_card_select(
                    name="story_format",
                    options=[
                        {"value": "novel", "label": "Novel", "icon": "📖"},
                        {"value": "screenplay", "label": "Screenplay", "icon": "🎬"},
                        {"value": "short", "label": "Short Story", "icon": "📝"},
                    ],
                    selected="novel",
                    label="Story Format",
                ),
            ),
            _showcase_card(
                "Form Modal",
                vstack(
                    form_modal(
                        field(input(name="name", placeholder="Enter name"), label="Name"),
                        field(
                            select(
                                name="type",
                                options=[("a", "Type A"), ("b", "Type B")],
                                placeholder="Select type...",
                            ),
                            label="Type",
                        ),
                        field(textarea(name="notes", placeholder="Notes..."), label="Notes"),
                        modal_id="showcase-form-modal",
                        title="Create Item",
                        form_action="/api/items",
                        submit_label="Create",
                    ),
                    text(
                        "(Use showModal() to open - combines modal + form)",
                        variant="caption",
                    ),
                    gap=2,
                ),
            ),
            _showcase_card(
                "Hero Card",
                grid(
                    hero_card(
                        title="Featured Location",
                        subtitle="Central District",
                        badge_text="5 Scenes",
                        image_url="https://picsum.photos/seed/hero1/400/225",
                        href="#",
                    ),
                    hero_card(
                        title="Ancient Temple",
                        subtitle="Sacred Grounds",
                        badge_text="Story Hub",
                    ),
                    columns=2,
                    gap="1rem",
                ),
            ),
            _showcase_card(
                "HTMX File Dropzone",
                htmx_file_dropzone(
                    upload_url="/api/upload",
                    accept=".csv,.xlsx",
                    max_size="10MB",
                ),
            ),
            _showcase_card(
                "HTMX Pagination",
                htmx_pagination(current_page=2, total_pages=10, base_url="/items"),
            ),
            _showcase_card(
                "HTMX Tag Manager",
                htmx_tag_manager(
                    available_tags=[
                        TagItem(id="1", name="Important", color="var(--color-red-500)"),
                        TagItem(id="2", name="Review", color="var(--color-blue-500)"),
                    ],
                    selected_tag_ids=["1"],
                    add_tag_url="/api/tags/add",
                    remove_tag_url="/api/tags/remove",
                ),
            ),
            _showcase_card(
                "Icon Card",
                grid(
                    icon_card(
                        title="Characters",
                        description="Manage your story's cast of characters",
                        icon_name="users",
                        href="#",
                    ),
                    icon_card(
                        title="Locations",
                        description="Explore and create world locations",
                        icon_name="map-pin",
                        icon_color="var(--theme-accent-secondary, #a855f7)",
                    ),
                    columns=2,
                    gap="1rem",
                ),
            ),
            _showcase_card(
                "Image Uploader",
                image_uploader(
                    entity_type="character",
                    entity_id="char-123",
                    project_id="proj-456",
                    current_image_url="https://ui-avatars.com/api/?name=Demo",
                    image_type="avatar",
                    label="Character Avatar",
                    form_id="demo-form",
                    field_name="avatar_url",
                ),
            ),
            _showcase_card(
                "Item Details",
                item_details(
                    [
                        ("ID", "12345"),
                        ("Name", "Example Item"),
                        ("Category", "General"),
                        ("Location", "Warehouse A"),
                        ("Notes", "Handle with care"),
                    ]
                ),
            ),
            _showcase_card(
                "Job Status Banner",
                job_status_banner(
                    [
                        BackgroundJob(
                            request_id="job-1",
                            job_name="Data Import",
                            status="running",
                            is_running=True,
                            created_at="2024-01-15 10:30:00",
                        ),
                        BackgroundJob(
                            request_id="job-2",
                            job_name="Report Generation",
                            status="completed",
                            is_running=False,
                            created_at="2024-01-15 09:00:00",
                        ),
                    ]
                ),
            ),
            _showcase_card(
                "Loading Screen",
                box(
                    loading_screen(message="Loading data..."),
                    style="height: 150px; position: relative;",
                ),
            ),
            _showcase_card(
                "Nav Card",
                hstack(
                    nav_card(
                        "Navigation",
                        "A link to another page",
                        href="/example",
                    ),
                    dashboard_nav_card(
                        "Dashboard Nav",
                        "Fancy neon card for dashboard nav",
                        href="#",
                        icon_content=Div("🚀", style="font-size: 2rem"),
                    ),
                    gap=3,
                ),
            ),
            _showcase_card(
                "Overflow Tooltip",
                overflow_tooltip(
                    "This is a very long text that will be truncated and shown in a tooltip when hovered over by the user",
                    max_width="200px",
                ),
            ),
            _showcase_card(
                "Removable Entity Row",
                vstack(
                    removable_entity_row(
                        name="John Doe",
                        remove_url="/api/remove/1",
                        remove_target="#row-1",
                        image_url="https://ui-avatars.com/api/?name=John+Doe",
                    ),
                    removable_entity_row(
                        name="Jane Smith",
                        remove_url="/api/remove/2",
                        remove_target="#row-2",
                    ),
                    gap=2,
                ),
            ),
            _showcase_card(
                "Result Card",
                hstack(
                    result_card(
                        item_id="ABC-001",
                        item_name="Example Result Item",
                        detail_url="#",
                        push_url=False,
                    ),
                    result_card(
                        item_id="XYZ-999",
                        item_name="Another Item with a Longer Name That May Wrap",
                        detail_url="#",
                        push_url=False,
                    ),
                    gap=3,
                    style="flex-wrap: wrap;",
                ),
            ),
            _showcase_card(
                "Search Bar",
                search_bar(placeholder="Search items...", width="100%"),
            ),
            _showcase_card(
                "Search Results",
                search_results(
                    results=[
                        {"id": 1, "name": "First Result Item"},
                        {"id": 2, "name": "Second Result Item"},
                    ],
                    query="result",
                ),
            ),
            _showcase_card(
                "Stat Card",
                hstack(
                    stat_card("Total Users", "1,234", icon="👤"),
                    stat_card(
                        "Revenue",
                        "$50,000",
                        icon="💰",
                        gradient_start="#f59e0b",
                        gradient_end="#ef4444",
                    ),
                    dashboard_stat_card(
                        "Neon Stat",
                        "450",
                        total="500",
                        icon=Div("✨", style="font-size: 1.5rem"),
                        progress_value=90,
                    ),
                    gap=3,
                    style="flex-wrap: wrap;",
                ),
            ),
            _showcase_card(
                "Stats Chart",
                stats_chart(
                    label_top="Speed",
                    label_left="Power",
                    label_right="Skill",
                ),
            ),
            _showcase_card(
                "Tab State Wrapper",
                vstack(
                    text("Loading state:", variant="caption"),
                    tab_state_wrapper(text("Content"), is_loading=True),
                    separator(),
                    text("Error state:", variant="caption"),
                    tab_state_wrapper(text("Content"), error="Failed to load"),
                    separator(),
                    text("Empty state:", variant="caption"),
                    tab_state_wrapper(text("Content"), has_data=False),
                    gap=2,
                ),
            ),
            _showcase_card(
                "Tag Manager",
                tag_manager(
                    available_tags=[
                        TagItem(id="1", name="Important", color="var(--color-red-500)"),
                        TagItem(id="2", name="Review", color="var(--color-blue-500)"),
                        TagItem(id="3", name="Approved", color="var(--color-green-500)"),
                    ],
                    selected_tags=[TagItem(id="1", name="Important")],
                ),
            ),
            _showcase_card(
                "Timeline Card",
                hstack(
                    timeline_card(
                        title="Phase 1",
                        item_type="Planning",
                        status="Complete",
                        sequence_position="Start",
                        href="#",
                    ),
                    timeline_card(
                        title="Phase 2",
                        item_type="Development",
                        status="In Progress",
                        sequence_position="Current",
                        image_url="https://picsum.photos/280/400",
                        href="#",
                    ),
                    gap=3,
                    style="flex-wrap: wrap;",
                ),
            ),
            _showcase_card(
                "Timeline Event Card",
                timeline_event_card(
                    event_id="evt-1",
                    title="Battle of Winterfell",
                    event_type="Battle",
                    date="Year 305",
                    description="Epic confrontation in the frozen north",
                    view_url="/timeline/evt-1",
                ),
            ),
            _showcase_card(
                "Timeline Lane",
                timeline_lane(
                    title="Main Story Arc",
                    items=[
                        {
                            "title": "Beginning",
                            "date": "Day 1",
                            "icon_color": "var(--color-blue-500)",
                            "href": "#",
                        },
                        {
                            "title": "Conflict",
                            "date": "Day 10",
                            "icon_color": "var(--color-red-500)",
                            "href": "#",
                        },
                    ],
                ),
            ),
            _showcase_card(
                "Token Pill",
                hstack(
                    token_pill(Token(id="1", name="Aspirin", type="Drug")),
                    token_pill(Token(id="2", name="BRCA1", type="Gene")),
                    token_pill({"id": "3", "name": "Cancer", "type": "Disease"}),
                    gap=2,
                ),
            ),
            _showcase_card(
                "User Actions",
                user_actions(
                    user_avatar=None,
                    user_name="Jane Smith",
                    menu_items=[
                        UserAction(id="profile", label="Profile", href="/profile", icon="👤"),
                        UserAction(id="settings", label="Settings", href="/settings", icon="⚙️"),
                        UserAction(
                            id="logout", label="Logout", href="/logout", icon="🚪", variant="danger"
                        ),
                    ],
                    notification_count=3,
                ),
            ),
            _showcase_card(
                "User Nav",
                user_nav(user={"email": "user@example.com", "name": "John Doe"}),
            ),
            _showcase_card(
                "Scene Card",
                hstack(
                    scene_card(
                        title="Opening Scene",
                        characters=[
                            {"name": "Alice", "avatar_url": None},
                            {"name": "Bob", "avatar_url": None},
                        ],
                        location_name="Central Plaza",
                        status="draft",
                        href="/stories/1/scenes/1",
                    ),
                    scene_card(
                        title="The Confrontation",
                        characters=[
                            {"name": "Hero", "avatar_url": None},
                        ],
                        location_name="Dark Castle",
                        status="complete",
                        accent_color="#ff6b6b",
                    ),
                    gap=3,
                    style="flex-wrap: wrap;",
                ),
            ),
            gap=4,
        ),
        open=True,
    )


def _organisms_showcase() -> Any:
    """Organisms Section."""
    return collapsible(
        heading("Organisms", level=2, style="color: var(--color-primary-600);"),
        vstack(
            _showcase_card(
                "Alphabet Browser",
                alphabet_browser(),
            ),
            _showcase_card(
                "Articles Search",
                articles_search(
                    tokens=[
                        SearchToken(id="DOID:123", name="Cancer", type="disease"),
                        SearchToken(id="GENE:456", name="BRCA1", type="gene"),
                    ],
                    placeholder="Add concept...",
                    suggestions_url="/api/concepts/search",
                    search_url="/api/articles/search",
                ),
            ),
            _showcase_card(
                "Data Table",
                data_table(
                    card(text("Row 1 content"), style="padding: 1rem;"),
                    card(text("Row 2 content"), style="padding: 1rem;"),
                    card(text("Row 3 content"), style="padding: 1rem;"),
                    title="Items",
                    search_value="example",
                    result_count=3,
                ),
            ),
            _showcase_card(
                "Feature Card",
                hstack(
                    feature_card(
                        title="Fast Development",
                        description="Build UIs quickly with pre-built components.",
                        icon="⚡",
                        progress=75,
                    ),
                    feature_card(
                        title="Consistent Design",
                        description="Maintain design consistency across your app.",
                        icon="🎨",
                        progress=90,
                    ),
                    gap=3,
                    style="flex-wrap: wrap;",
                ),
            ),
            _showcase_card(
                "Header",
                header(
                    logo_text="MyApp",
                    logo_href="/",
                    breadcrumb_items=[
                        {"label": "Home", "url": "/"},
                        {"label": "Settings"},
                    ],
                    user_name="John Doe",
                    notification_count=5,
                ),
            ),
            _showcase_card(
                "Hero Section",
                hero_section(
                    headline="Build Amazing Apps",
                    subheadline="Create stunning user interfaces with our component library.",
                    cta_text="Get Started",
                    cta_link="#",
                ),
            ),
            _showcase_card(
                "Navigation",
                vstack(
                    text("Authenticated user:", variant="caption"),
                    navigation(user={"email": "john@example.com", "name": "John Doe"}),
                    text("Unauthenticated with CTA:", variant="caption"),
                    navigation(show_cta=True),
                    gap=3,
                ),
            ),
            _showcase_card(
                "Notifications",
                notifications(
                    items=[
                        NotificationItem(
                            id="1",
                            type="info",
                            message="New update available",
                            is_read=False,
                            created_at="2024-01-15 10:30:00",
                        ),
                        NotificationItem(
                            id="2",
                            type="success",
                            message="Export completed",
                            is_read=True,
                            created_at="2024-01-15 09:00:00",
                        ),
                    ],
                    hx_mark_all_read="/api/notifications/read-all",
                ),
            ),
            _showcase_card(
                "Page Header",
                page_header(
                    title="Dashboard",
                    breadcrumb_items=[
                        {"label": "Home", "url": "/"},
                        {"label": "Dashboard"},
                    ],
                    actions=[
                        button("Export", variant="outline", size="sm"),
                        button("Add New", variant="solid", size="sm"),
                    ],
                    description="Overview of your data",
                ),
            ),
            _showcase_card(
                "Profile Card",
                profile_card(
                    user={
                        "name": "Jane Doe",
                        "email": "jane.doe@example.com",
                        "picture": "https://i.pravatar.cc/150?u=jane",
                    }
                ),
            ),
            _showcase_card(
                "Timeline View",
                timeline_view(
                    items_data=[
                        {
                            "id": "1",
                            "title": "Phase 1: Discovery",
                            "item_type": "Research",
                            "status": "Complete",
                            "sequence_position": "Start",
                        },
                        {
                            "id": "2",
                            "title": "Phase 2: Development",
                            "item_type": "Implementation",
                            "status": "In Progress",
                            "sequence_position": "Current",
                        },
                        {
                            "id": "3",
                            "title": "Phase 3: Launch",
                            "item_type": "Deployment",
                            "status": "Planning",
                            "sequence_position": "Next",
                        },
                    ],
                    href_template="/phases/{id}",
                ),
            ),
            _showcase_card(
                "Kanban Board",
                kanban_board(
                    kanban_column(
                        "Act 1",
                        scene_card(
                            title="Opening",
                            characters=[{"name": "Hero", "avatar_url": None}],
                            location_name="Village",
                            status="complete",
                        ),
                        scene_card(
                            title="Call to Adventure",
                            characters=[{"name": "Hero", "avatar_url": None}],
                            location_name="Forest",
                            status="draft",
                        ),
                        accent_color="#00f0ff",
                    ),
                    kanban_column(
                        "Act 2",
                        scene_card(
                            title="The Journey",
                            characters=[
                                {"name": "Hero", "avatar_url": None},
                                {"name": "Mentor", "avatar_url": None},
                            ],
                            location_name="Mountains",
                            status="draft",
                        ),
                        accent_color="#f0f000",
                    ),
                    kanban_column(
                        "Act 3",
                        empty_message="No scenes yet",
                        accent_color="#ff6b6b",
                    ),
                    min_height="300px",
                ),
            ),
            _showcase_card(
                "Relationship Board",
                text(
                    "Kanban-style board for managing entity relationships grouped by verb. "
                    "Uses HTMX for dynamic updates without nested forms.",
                    variant="caption",
                    style="margin-bottom: 1rem;",
                ),
                relationship_board(
                    items=[
                        ("loc-1", "Dark Castle", "Born in", "Year 1023", None, None),
                        ("loc-2", "Crystal Cave", "Born in", None, None, None),
                        ("loc-3", "Mountain Peak", "Visits", "Frequently", None, None),
                        ("char-1", "The Mentor", "Knows secret", "Ancient prophecy", None, None),
                    ],
                    add_url=None,
                    options=[("loc-4", "Forest"), ("loc-5", "Village")],
                    is_editing=False,
                    item_icon="map-pin",
                    dom_id="showcase-relationship-board",
                ),
            ),
            gap=4,
        ),
        open=True,
    )


def _templates_showcase() -> Any:
    """Templates Section."""
    return collapsible(
        heading("Templates", level=2, style="color: var(--color-primary-600);"),
        vstack(
            _showcase_card(
                "Auth Page Layout",
                text(
                    "Centered layout for authentication pages (login, signup, etc.)",
                    variant="caption",
                ),
                box(
                    auth_page_layout(
                        card(
                            vstack(
                                heading("Login", level=3),
                                text("Authentication form goes here"),
                                gap=2,
                            ),
                            style="padding: 1.5rem;",
                        ),
                        max_width="300px",
                    ),
                    style="height: 200px; border: 1px dashed var(--color-gray-300); border-radius: 8px; overflow: hidden; background: var(--color-gray-50);",
                ),
            ),
            _showcase_card(
                "Base Page",
                text(
                    "Base page template provides consistent HTML structure with head, styles, and HTMX. "
                    "Used internally by other templates - returns complete Html document.",
                    variant="caption",
                ),
                vstack(
                    text("Features:", weight="semibold"),
                    text("• Automatic meta viewport and charset", variant="caption"),
                    text("• Design system base and component styles", variant="caption"),
                    text("• Optional HTMX integration", variant="caption"),
                    text("• Menu click-outside handling script", variant="caption"),
                    text(
                        "• Custom extra_head support for additional scripts/styles",
                        variant="caption",
                    ),
                    gap=1,
                    style="align-items: flex-start;",
                ),
            ),
            _showcase_card(
                "Centered Content",
                box(
                    centered_content(
                        vstack(
                            heading("Centered", level=3),
                            text("Content centered horizontally"),
                            gap=2,
                        ),
                        max_width="300px",
                    ),
                    style="height: 150px; background: var(--color-gray-50); border-radius: 8px;",
                ),
            ),
            _showcase_card(
                "Error Template",
                text(
                    "Error template provides consistent error page layout (404, 500, etc.)",
                    variant="caption",
                ),
                box(
                    error_template(
                        error_code="404",
                        title="Page Not Found",
                        description="The page you're looking for doesn't exist.",
                        primary_action_text="Go Home",
                        primary_action_href="/",
                    ),
                    style="height: 300px; border: 1px dashed var(--color-gray-300); border-radius: 8px; overflow: hidden;",
                ),
            ),
            _showcase_card(
                "Labs Intro Page",
                text(
                    "Feature landing page template for Labs applications with hero section and content card.",
                    variant="caption",
                ),
                box(
                    labs_intro_page(
                        feature_title="Feature",
                        feature_subtitle="Explore this exciting new feature",
                        hero_title="Feature Overview",
                        descriptions=[
                            "This is the first paragraph describing the feature.",
                            "Additional details about what makes this feature special.",
                        ],
                        launch_url="#",
                        launch_button_text="Launch Feature",
                        badges=[
                            BadgeConfig("Incubating", "brand"),
                            BadgeConfig("Beta", "gray"),
                        ],
                        last_update="November 2024",
                    ),
                    style="height: 400px; border: 1px dashed var(--color-gray-300); border-radius: 8px; overflow: auto;",
                ),
            ),
            _showcase_card(
                "Page Container",
                box(
                    page_container(
                        vstack(
                            text("Full-height page container"),
                            text("Provides consistent background", variant="caption"),
                            gap=2,
                        ),
                        min_height="100px",
                        padding="1rem",
                    ),
                    style="border: 1px dashed var(--color-gray-300); border-radius: 8px;",
                ),
            ),
            _showcase_card(
                "Sidebar Layout",
                box(
                    sidebar_layout(
                        vstack(
                            text("Main content area"),
                            text("This is where primary content goes", variant="caption"),
                            gap=2,
                        ),
                        sidebar=vstack(
                            text("Sidebar", weight="semibold"),
                            text("Filters, nav, etc.", variant="caption"),
                            gap=2,
                        ),
                        sidebar_width="150px",
                    ),
                    style="height: 200px; border: 1px dashed var(--color-gray-300); border-radius: 8px; overflow: hidden;",
                ),
            ),
            gap=4,
        ),
        open=True,
    )


def ui_showcase_page(
    title: str = "Component Library Showcase",
    theme_id: str | None = None,
) -> Any:
    """
    Comprehensive UI showcase demonstrating all components.

    Args:
        title: Page title
        theme_id: Optional theme ID to apply (e.g., "space", "ocean", "light")

    Returns:
        Complete HTML page with UI showcase
    """
    content = vstack(
        # Header
        vstack(
            hstack(
                button_link("← Home", href="/", variant="outline", size="sm"),
                style="width: 100%;",
            ),
            heading(title, level=1),
            text(
                "Complete showcase of atoms, molecules, organisms, and templates",
                variant="caption",
            ),
            gap=2,
        ),
        separator(),
        # Component sections
        _atoms_showcase(),
        _molecules_showcase(),
        _organisms_showcase(),
        _templates_showcase(),
        separator(),
        # Footer
        vstack(
            text("Built with components-library-fasthtml", variant="caption"),
            button_link("← Back to Home", href="/", variant="solid", color_palette="brand"),
            gap=2,
            style="text-align: center;",
        ),
        gap=6,
        style="max-width: 64rem; margin: 0 auto; padding: 2rem;",
    )

    # Generate theme CSS if a theme is specified
    extra_head = None
    if theme_id:
        extra_head = f"<style>{get_theme_css(theme_id)}</style>"

    return base_page(content, title=title, extra_head=extra_head)
