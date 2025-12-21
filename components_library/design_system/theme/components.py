"""Component-specific theme styles."""

from __future__ import annotations

from typing import Literal

from ..tokens import (
    BorderRadius,
    BorderWidth,
    Breakpoints,
    Colors,
    Shadows,
    Spacing,
    Transitions,
    Typography,
    ZIndex,
)

colors = Colors()
spacing = Spacing()
typography = Typography()
shadows = Shadows()
radius = BorderRadius()
borders = BorderWidth()
transitions = Transitions()
z_index = ZIndex()
breakpoints = Breakpoints()


def _generate_box_shadow(level: Literal["sm", "md", "lg", "xl"] = "md") -> str:
    """Generate box shadow CSS value."""
    shadow_map = {
        "sm": shadows.sm,
        "md": shadows.md,
        "lg": shadows.lg,
        "xl": shadows.xl,
    }
    return shadow_map[level]


def _layout_component_styles() -> str:
    """Generate layout component styles (box, flex, grid, stack, separator)."""
    return f"""
        /* ===== LAYOUT COMPONENTS ===== */

        /* Box */
        .box {{
            display: block;
        }}

        /* Flex */
        .flex {{
            display: flex;
        }}

        .flex-row {{ flex-direction: row; }}
        .flex-col {{ flex-direction: column; }}
        .flex-wrap {{ flex-wrap: wrap; }}

        .items-start {{ align-items: flex-start; }}
        .items-center {{ align-items: center; }}
        .items-end {{ align-items: flex-end; }}
        .items-stretch {{ align-items: stretch; }}

        .justify-start {{ justify-content: flex-start; }}
        .justify-center {{ justify-content: center; }}
        .justify-end {{ justify-content: flex-end; }}
        .justify-between {{ justify-content: space-between; }}
        .justify-around {{ justify-content: space-around; }}

        /* Grid */
        .grid {{
            display: grid;
        }}

        .grid-cols-1 {{ grid-template-columns: repeat(1, minmax(0, 1fr)); }}
        .grid-cols-2 {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
        .grid-cols-3 {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
        .grid-cols-4 {{ grid-template-columns: repeat(4, minmax(0, 1fr)); }}

        /* Stack */
        .vstack {{
            display: flex;
            flex-direction: column;
        }}

        .hstack {{
            display: flex;
            flex-direction: row;
            align-items: center;
        }}

        /* Separator */
        .separator {{
            border: none;
            background-color: {colors.border};
        }}

        .separator-horizontal {{
            height: {borders.default};
            width: 100%;
            margin: {spacing._4} 0;
        }}

        .separator-vertical {{
            width: {borders.default};
            height: 100%;
            margin: 0 {spacing._4};
        }}
        """


def _button_component_styles() -> str:
    """Generate button component styles."""
    return f"""
        /* ===== BUTTON COMPONENTS ===== */

        .btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: {spacing._2};
            padding: {spacing._2_5} {spacing._4};
            border: {borders.default} solid transparent;
            border-radius: {radius.md};
            font-size: {typography.base.size};
            font-weight: {typography.font_medium};
            line-height: {typography.base.line_height};
            text-decoration: none;
            cursor: pointer;
            transition: all {transitions.base} {transitions.ease_in_out};
            white-space: nowrap;
            user-select: none;
        }}

        /* Button sizes */
        .btn-xs {{
            padding: {spacing._1} {spacing._2};
            font-size: {typography.xs.size};
            min-height: 28px;
        }}

        .btn-sm {{
            padding: {spacing._2} {spacing._3};
            font-size: {typography.sm.size};
            min-height: 36px;
        }}

        .btn-md {{
            padding: {spacing._2_5} {spacing._4};
            font-size: {typography.base.size};
            min-height: 40px;
        }}

        .btn-lg {{
            padding: {spacing._3} {spacing._6};
            font-size: {typography.lg.size};
            min-height: 48px;
        }}

        .btn-xl {{
            padding: {spacing._4} {spacing._8};
            font-size: {typography.xl.size};
            min-height: 56px;
        }}

        /* Button variants - Primary/Brand */
        .btn-solid.btn-brand {{
            background-color: {colors.primary.s600};
            color: white;
        }}

        .btn-solid.btn-brand:hover:not(:disabled) {{
            background-color: {colors.primary.s700};
        }}

        .btn-solid.btn-brand:active:not(:disabled) {{
            background-color: {colors.primary.s800};
        }}

        .btn-outline.btn-brand {{
            background-color: transparent;
            color: {colors.primary.s600};
            border-color: {colors.primary.s600};
        }}

        .btn-outline.btn-brand:hover:not(:disabled) {{
            background-color: {colors.primary.s50};
        }}

        .btn-ghost.btn-brand {{
            background-color: transparent;
            color: {colors.primary.s600};
        }}

        .btn-ghost.btn-brand:hover:not(:disabled) {{
            background-color: {colors.primary.s50};
        }}

        /* Button variants - Other colors */
        .btn-solid.btn-gray {{
            background-color: {colors.neutral.s600};
            color: white;
        }}

        .btn-solid.btn-gray:hover:not(:disabled) {{
            background-color: {colors.neutral.s700};
        }}

        .btn-solid.btn-red {{
            background-color: {colors.error.s600};
            color: white;
        }}

        .btn-solid.btn-red:hover:not(:disabled) {{
            background-color: {colors.error.s700};
        }}

        .btn-solid.btn-green {{
            background-color: {colors.success.s600};
            color: white;
        }}

        .btn-solid.btn-green:hover:not(:disabled) {{
            background-color: {colors.success.s700};
        }}

        /* Button states */
        .btn:disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}

        .btn-loading {{
            position: relative;
            color: transparent;
            pointer-events: none;
        }}

        .btn-loading::after {{
            content: "";
            position: absolute;
            width: 16px;
            height: 16px;
            top: 50%;
            left: 50%;
            margin-left: -8px;
            margin-top: -8px;
            border: 2px solid currentColor;
            border-radius: 50%;
            border-top-color: transparent;
            animation: button-spin 0.6s linear infinite;
        }}

        @keyframes button-spin {{
            to {{ transform: rotate(360deg); }}
        }}

        /* Icon Button */
        .icon-btn {{
            padding: {spacing._2};
            aspect-ratio: 1;
        }}
        """


def _input_component_styles() -> str:
    """Generate input component styles."""
    return f"""
        /* ===== INPUT COMPONENTS ===== */

        .input {{
            display: block;
            width: 100%;
            padding: {spacing._2_5} {spacing._3_5};
            border: {borders.default} solid {colors.border};
            border-radius: {radius.md};
            font-size: {typography.base.size};
            line-height: {typography.base.line_height};
            color: {colors.text_primary};
            background-color: {colors.background};
            transition: border-color {transitions.base}, box-shadow {transitions.base};
        }}

        .input:focus {{
            border-color: {colors.border_focus};
            outline: none;
            box-shadow: 0 0 0 3px {colors.primary.s100};
        }}

        .input:disabled {{
            background-color: {colors.background_alt};
            color: {colors.text_disabled};
            cursor: not-allowed;
        }}

        .input-sm {{
            padding: {spacing._2} {spacing._3};
            font-size: {typography.sm.size};
        }}

        .input-lg {{
            padding: {spacing._3} {spacing._4};
            font-size: {typography.lg.size};
        }}

        .input-error {{
            border-color: {colors.error.s600};
        }}

        .input-error:focus {{
            box-shadow: 0 0 0 3px {colors.error.s100};
        }}

        /* Textarea */
        .textarea {{
            resize: vertical;
            min-height: 80px;
        }}

        /* Select */
        .select {{
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3E%3Cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3E%3C/svg%3E");
            background-position: right {spacing._2_5} center;
            background-repeat: no-repeat;
            background-size: 1.5em 1.5em;
            padding-right: {spacing._10};
        }}

        /* Checkbox & Radio */
        .checkbox,
        .radio {{
            width: 1.125rem;
            height: 1.125rem;
            border: {borders._2} solid {colors.border};
            cursor: pointer;
            transition: all {transitions.fast};
        }}

        .checkbox {{
            border-radius: {radius.sm};
        }}

        .radio {{
            border-radius: {radius.full};
        }}

        .checkbox:checked,
        .radio:checked {{
            background-color: {colors.primary.s600};
            border-color: {colors.primary.s600};
        }}

        .checkbox:focus,
        .radio:focus {{
            outline: none;
            box-shadow: 0 0 0 3px {colors.primary.s100};
        }}

        /* Switch */
        .switch {{
            position: relative;
            display: inline-block;
            width: 44px;
            height: 24px;
        }}

        .switch input {{
            opacity: 0;
            width: 0;
            height: 0;
        }}

        .switch-slider {{
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: {colors.neutral.s300};
            transition: {transitions.base};
            border-radius: {radius.full};
        }}

        .switch-slider:before {{
            position: absolute;
            content: "";
            height: 18px;
            width: 18px;
            left: 3px;
            bottom: 3px;
            background-color: white;
            transition: {transitions.base};
            border-radius: {radius.full};
        }}

        .switch input:checked + .switch-slider {{
            background-color: {colors.primary.s600};
        }}

        .switch input:checked + .switch-slider:before {{
            transform: translateX(20px);
        }}

        /* Field (form field wrapper) */
        .field {{
            margin-bottom: {spacing._4};
        }}

        .field-label {{
            display: block;
            margin-bottom: {spacing._2};
            font-size: {typography.sm.size};
            font-weight: {typography.font_medium};
            color: {colors.text_primary};
        }}

        .field-helper {{
            margin-top: {spacing._1};
            font-size: {typography.sm.size};
            color: {colors.text_secondary};
        }}

        .field-error {{
            margin-top: {spacing._1};
            font-size: {typography.sm.size};
            color: {colors.error.s600};
        }}
        """


def _feedback_component_styles() -> str:
    """Generate feedback component styles (alert, spinner, progress, badge, tag)."""
    return f"""
        /* ===== FEEDBACK COMPONENTS ===== */

        /* Alert */
        .alert {{
            padding: {spacing._4};
            border-radius: {radius.md};
            border-left: 4px solid;
            display: flex;
            gap: {spacing._3};
        }}

        .alert-info {{
            background-color: {colors.primary.s50};
            border-color: {colors.primary.s600};
            color: {colors.primary.s900};
        }}

        .alert-success {{
            background-color: {colors.success.s50};
            border-color: {colors.success.s600};
            color: {colors.success.s900};
        }}

        .alert-warning {{
            background-color: {colors.warning.s50};
            border-color: {colors.warning.s600};
            color: {colors.warning.s900};
        }}

        .alert-error {{
            background-color: {colors.error.s50};
            border-color: {colors.error.s600};
            color: {colors.error.s900};
        }}

        /* Spinner */
        .spinner {{
            display: inline-block;
            width: 24px;
            height: 24px;
            border: 3px solid {colors.neutral.s200};
            border-top-color: {colors.primary.s600};
            border-radius: {radius.full};
            animation: spin 0.6s linear infinite;
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}

        .spinner-sm {{ width: 16px; height: 16px; border-width: 2px; }}
        .spinner-lg {{ width: 32px; height: 32px; border-width: 4px; }}

        /* Progress */
        .progress {{
            width: 100%;
            height: 8px;
            background-color: {colors.neutral.s200};
            border-radius: {radius.full};
            overflow: hidden;
        }}

        .progress-bar {{
            height: 100%;
            background-color: {colors.primary.s600};
            transition: width {transitions.slow} {transitions.ease_out};
        }}

        /* Skeleton */
        .skeleton {{
            background: linear-gradient(
                90deg,
                {colors.neutral.s200} 25%,
                {colors.neutral.s100} 50%,
                {colors.neutral.s200} 75%
            );
            background-size: 200% 100%;
            animation: skeleton-loading 1.5s ease-in-out infinite;
            border-radius: {radius.md};
        }}

        @keyframes skeleton-loading {{
            0% {{ background-position: 200% 0; }}
            100% {{ background-position: -200% 0; }}
        }}

        /* Badge */
        .badge {{
            display: inline-flex;
            align-items: center;
            padding: {spacing._0_5} {spacing._2};
            font-size: {typography.xs.size};
            font-weight: {typography.font_medium};
            border-radius: {radius.full};
        }}

        .badge-brand {{
            background-color: {colors.primary.s100};
            color: {colors.primary.s800};
        }}

        .badge-gray {{
            background-color: {colors.neutral.s100};
            color: {colors.neutral.s800};
        }}

        .badge-success {{
            background-color: {colors.success.s100};
            color: {colors.success.s800};
        }}

        .badge-error {{
            background-color: {colors.error.s100};
            color: {colors.error.s800};
        }}

        .badge-outline {{
            background-color: transparent;
            border: 1px solid {colors.neutral.s300};
            color: {colors.text_secondary};
        }}

        /* Tag */
        .tag {{
            display: inline-flex;
            align-items: center;
            gap: {spacing._1};
            padding: {spacing._1} {spacing._2_5};
            font-size: {typography.sm.size};
            border-radius: {radius.md};
            background-color: {colors.neutral.s100};
            color: {colors.text_primary};
        }}

        .tag-close {{
            cursor: pointer;
            padding: 0;
            border: none;
            background: none;
            color: {colors.text_secondary};
            font-size: 1.125rem;
            line-height: 1;
        }}

        .tag-close:hover {{
            color: {colors.text_primary};
        }}
        """


def _card_table_component_styles() -> str:
    """Generate card and table component styles."""
    return f"""
        /* ===== CARD COMPONENT ===== */

        .card {{
            background-color: {colors.background};
            border: {borders.default} solid {colors.border};
            border-radius: {radius.lg};
            box-shadow: {shadows.sm};
            overflow: hidden;
        }}

        .card-header {{
            padding: {spacing._6};
            border-bottom: {borders.default} solid {colors.border};
        }}

        .card-body {{
            padding: {spacing._6};
        }}

        .card-footer {{
            padding: {spacing._6};
            border-top: {borders.default} solid {colors.border};
            background-color: {colors.background_alt};
        }}

        /* ===== TABLE COMPONENT ===== */

        .table {{
            width: 100%;
            border-collapse: collapse;
        }}

        .table th {{
            padding: {spacing._3} {spacing._4};
            text-align: left;
            font-weight: {typography.font_semibold};
            font-size: {typography.sm.size};
            color: {colors.text_secondary};
            border-bottom: {borders._2} solid {colors.border};
            background-color: {colors.background_alt};
        }}

        .table td {{
            padding: {spacing._3} {spacing._4};
            border-bottom: {borders.default} solid {colors.border};
        }}

        .table tr:hover {{
            background-color: {colors.background_alt};
        }}
        """


def _modal_overlay_component_styles() -> str:
    """Generate modal and overlay component styles."""
    return f"""
        /* ===== MODAL COMPONENT (Native dialog element) ===== */

        /* Native dialog backdrop */
        dialog.modal::backdrop {{
            background-color: rgba(0, 0, 0, 0.5);
        }}

        dialog.modal {{
            background-color: {colors.background};
            border-radius: {radius.lg};
            box-shadow: {shadows.xl};
            max-width: 32rem;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            border: none;
            padding: 0;
        }}

        /* Center dialog on screen */
        dialog.modal[open] {{
            display: block;
        }}

        .modal-header {{
            padding: {spacing._6};
            border-bottom: {borders.default} solid {colors.border};
        }}

        .modal-body {{
            padding: {spacing._6};
        }}

        .modal-footer {{
            padding: {spacing._6};
            border-top: {borders.default} solid {colors.border};
            display: flex;
            justify-content: flex-end;
            gap: {spacing._3};
        }}
        """


def _tabs_accordion_component_styles() -> str:
    """Generate tabs and accordion component styles."""
    # Generate CSS for up to 10 tabs (radio-based switching)
    tab_switch_css = ""
    for i in range(1, 11):
        tab_switch_css += f"""
        .tab-radio:nth-of-type({i}):checked ~ .tabs-list .tab:nth-of-type({i}) {{
            color: {colors.primary.s600};
            border-bottom-color: {colors.primary.s600};
        }}
        .tab-radio:nth-of-type({i}):checked ~ .tabs-panels .tab-panel:nth-of-type({i}) {{
            display: block;
        }}
        """

    return f"""
        /* ===== TABS COMPONENT (Pure CSS with radio inputs) ===== */

        .tabs {{
            position: relative;
        }}

        /* Hide radio inputs (but keep accessible) */
        .tab-radio {{
            position: absolute;
            opacity: 0;
            pointer-events: none;
        }}

        .tabs-list {{
            display: flex;
            border-bottom: {borders._2} solid {colors.border};
            gap: {spacing._1};
        }}

        .tab {{
            padding: {spacing._3} {spacing._4};
            border: none;
            background: none;
            cursor: pointer;
            color: {colors.text_secondary};
            font-weight: {typography.font_medium};
            border-bottom: {borders._2} solid transparent;
            transition: all {transitions.fast};
            margin-bottom: -{borders._2};
        }}

        .tab:hover {{
            color: {colors.text_primary};
        }}

        /* Hide all panels by default */
        .tabs-panels .tab-panel {{
            display: none;
            padding: {spacing._6} 0;
        }}

        /* Radio-based tab switching (supports up to 10 tabs) */
        {tab_switch_css}

        /* ===== ACCORDION COMPONENT ===== */

        .accordion-item {{
            border-bottom: {borders.default} solid {colors.border};
        }}

        /* Hide default summary marker for accordion */
        .accordion-item > summary {{
            list-style: none;
        }}

        .accordion-item > summary::-webkit-details-marker {{
            display: none;
        }}

        .accordion-item > summary::marker {{
            display: none;
            content: "";
        }}

        .accordion-trigger {{
            width: 100%;
            padding: {spacing._4};
            text-align: left;
            background: none;
            border: none;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: {typography.font_medium};
            color: {colors.text_primary};
            transition: background-color {transitions.fast};
        }}

        .accordion-trigger:hover {{
            background-color: {colors.background_alt};
        }}

        /* Rotate icon when accordion is open */
        .accordion-item[open] .accordion-icon {{
            transform: rotate(180deg);
        }}

        .accordion-content {{
            padding: 0 {spacing._4} {spacing._4};
            color: {colors.text_secondary};
        }}
        """


def _htmx_search_component_styles() -> str:
    """Generate HTMX and search results component styles."""
    return f"""
        /* ===== HTMX SPECIFIC ===== */

        /* Loading states */
        .htmx-request {{
            opacity: 0.7;
            pointer-events: none;
        }}

        .htmx-swapping {{
            opacity: 0;
            transition: opacity {transitions.fast};
        }}

        .htmx-settling {{
            opacity: 1;
            transition: opacity {transitions.fast};
        }}

        /* Loading indicator */
        .htmx-indicator {{
            display: none;
        }}

        .htmx-request .htmx-indicator {{
            display: inline-block;
        }}

        .htmx-request.htmx-indicator {{
            display: inline-block;
        }}

        /* ===== SEARCH RESULTS GRID ===== */

        .search-results-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: {spacing._4};
            width: 100%;
        }}

        @media (min-width: {breakpoints.md}) {{
            .search-results-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}

        @media (min-width: {breakpoints.lg}) {{
            .search-results-grid {{
                grid-template-columns: repeat(3, 1fr);
            }}
        }}

        @media (min-width: {breakpoints.xl}) {{
            .search-results-grid {{
                grid-template-columns: repeat(4, 1fr);
            }}
        }}

        /* Enhanced test result cards */
        .search-result-item {{
            transition: all {transitions.base} {transitions.ease_in_out};
        }}

        .search-result-item:hover {{
            transform: translateY(-3px);
            box-shadow: {_generate_box_shadow("xl")};
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            border-left-color: #1d4ed8;
        }}

        .search-result-item:active {{
            transform: translateY(-1px);
            box-shadow: {_generate_box_shadow("md")};
        }}
        """


def _enhanced_item_details_styles() -> str:
    """Generate enhanced item details component styles."""
    return f"""
        /* ===== ENHANCED ITEM DETAILS ===== */

        .enhanced-item-details {{
            background: linear-gradient(
                135deg, {colors.background} 0%, {colors.neutral.s50} 100%
            );
            border-radius: {radius.xl};
            padding: {spacing._6};
            box-shadow: {shadows.lg};
            border: 1px solid {colors.border};
            position: relative;
            overflow: hidden;
        }}

        .enhanced-item-details::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(
                90deg, {colors.primary.s500} 0%, {colors.primary.s600} 50%,
                {colors.primary.s500} 100%
            );
        }}

        .enhanced-detail-card {{
            background: {colors.background};
            border: 1px solid {colors.border};
            border-radius: {radius.lg};
            box-shadow: {shadows.sm};
            transition: all {transitions.base} {transitions.ease_in_out};
            position: relative;
            overflow: hidden;
        }}

        .enhanced-detail-card:hover {{
            transform: translateY(-2px);
            box-shadow: {shadows.lg};
            border-color: {colors.primary.s300};
        }}

        .enhanced-detail-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(
                180deg, {colors.primary.s400} 0%, {colors.primary.s600} 100%
            );
            opacity: 0;
            transition: opacity {transitions.base} {transitions.ease_in_out};
        }}

        .enhanced-detail-card:hover::before {{
            opacity: 1;
        }}

        .enhanced-detail-row {{
            padding: {spacing._4};
            background: {colors.background};
            border-radius: {radius.lg};
            border: 1px solid {colors.border};
            transition: all {transitions.base} {transitions.ease_in_out};
            position: relative;
            overflow: hidden;
        }}

        .detail-icon-container {{
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .detail-icon {{
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            background: linear-gradient(
                135deg, {colors.primary.s100} 0%, {colors.primary.s200} 100%
            );
            border-radius: {radius.lg};
            border: 2px solid {colors.primary.s200};
            transition: all {transitions.base} {transitions.ease_in_out};
        }}

        .enhanced-detail-card:hover .detail-icon {{
            transform: scale(1.1);
            background: linear-gradient(
                135deg, {colors.primary.s200} 0%, {colors.primary.s300} 100%
            );
            border-color: {colors.primary.s300};
        }}

        .detail-content {{
            flex: 1;
        }}

        .detail-label {{
            color: {colors.text_secondary};
            font-size: {typography.sm.size};
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: {spacing._1};
            font-weight: {typography.font_semibold};
        }}

        .detail-value {{
            color: {colors.text_primary};
            font-size: {typography.base.size};
            line-height: 1.6;
            word-wrap: break-word;
            overflow-wrap: break-word;
            font-weight: {typography.font_medium};
        }}

        /* Animation for detail cards */
        .enhanced-detail-card {{
            animation: fadeInUp 0.3s ease-out;
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Staggered animation for multiple cards */
        .enhanced-detail-card:nth-child(1) {{ animation-delay: 0.1s; }}
        .enhanced-detail-card:nth-child(2) {{ animation-delay: 0.2s; }}
        .enhanced-detail-card:nth-child(3) {{ animation-delay: 0.3s; }}
        .enhanced-detail-card:nth-child(4) {{ animation-delay: 0.4s; }}
        .enhanced-detail-card:nth-child(5) {{ animation-delay: 0.5s; }}
        """


def _responsive_page_specific_styles() -> str:
    """Generate responsive utilities and page-specific component styles."""
    return f"""
        /* ===== RESPONSIVE UTILITIES ===== */

        @media (min-width: {breakpoints.md}) {{
            /* Touch targets for tablets */
            .btn, .input, .select, .checkbox, .radio {{
                min-height: 44px;
            }}
        }}

        /* ===== PAGE-SPECIFIC COMPONENT STYLES ===== */

        /* Lab test lookup card */
        .lab-test-lookup {{
            width: 100%;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            background: white;
        }}

        @media (max-width: {breakpoints.tablet}) {{
            .lab-test-lookup {{
                width: 100% !important;
                margin: 0 !important;
                padding: 1.25rem !important;
                box-sizing: border-box !important;
            }}
        }}

        /* Action buttons container */
        .action-buttons-container {{
            margin: 1rem 0;
        }}

        .action-buttons-container button {{
            min-width: 140px;
            flex: 1;
        }}

        @media (max-width: {breakpoints.tablet}) {{
            .action-buttons-container {{
                flex-direction: column !important;
            }}

            .action-buttons-container button {{
                width: 100% !important;
                min-width: auto !important;
            }}
        }}

        /* Info cards grid */
        .info-cards-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-top: 2rem;
            width: 100%;
        }}

        @media (max-width: {breakpoints.tablet}) {{
            .info-cards-grid {{
                grid-template-columns: 1fr;
                gap: 1rem;
            }}
        }}

        /* User profile card */
        .user-profile-card {{
            text-align: center;
            margin-top: 2rem;
        }}

        .user-avatar {{
            margin: 0 auto 1rem;
        }}

        .user-email {{
            font-family: monospace;
            background: var(--color-background-subtle);
            padding: 0.5rem;
            border-radius: 0.375rem;
            border: 1px solid var(--color-border-default);
        }}

        .user-description {{
            color: var(--color-text-muted);
            max-width: 400px;
            margin: 0 auto;
        }}

        .logout-button {{
            margin-top: 1rem;
        }}

        @media (max-width: {breakpoints.tablet}) {{
            .user-profile-card {{
                margin: 1rem;
                padding: 1.5rem;
            }}

            .user-avatar {{
                width: 80px;
                height: 80px;
            }}
        }}
        """


def _overlay_component_styles() -> str:
    """Generate overlay component styles (modal, popover, menu)."""
    return f"""
        /* ===== OVERLAY COMPONENTS ===== */

        /* Modal */
        .modal-backdrop {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: {z_index.modal};
            padding: {spacing._4};
        }}

        .modal {{
            background-color: {colors.background};
            border-radius: {radius.lg};
            box-shadow: {_generate_box_shadow("xl")};
            max-width: 500px;
            width: 100%;
            z-index: {z_index.modal};
            max-height: 90vh;
            overflow-y: auto;
        }}

        /* Popover */
        .popover-wrapper {{
            position: relative;
            display: inline-block;
        }}

        .popover {{
            position: absolute;
            z-index: {z_index.popover};
            background-color: {colors.background};
            border: {borders.default} solid {colors.border};
            border-radius: {radius.md};
            padding: {spacing._4};
            box-shadow: {_generate_box_shadow("md")};
            min-width: 200px;
        }}

        .popover-top {{
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            margin-bottom: {spacing._2};
        }}

        .popover-bottom {{
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            margin-top: {spacing._2};
        }}

        .popover-left {{
            right: 100%;
            top: 50%;
            transform: translateY(-50%);
            margin-right: {spacing._2};
        }}

        .popover-right {{
            left: 100%;
            top: 50%;
            transform: translateY(-50%);
            margin-left: {spacing._2};
        }}

        /* Menu */
        .menu-wrapper {{
            position: relative;
            display: inline-block;
        }}

        .menu {{
            position: absolute;
            z-index: {z_index.dropdown};
            background-color: {colors.background};
            border: {borders.default} solid {colors.border};
            border-radius: {radius.md};
            padding: {spacing._2} 0;
            box-shadow: {_generate_box_shadow("md")};
            min-width: 200px;
        }}

        .menu-bottom-left {{
            top: 100%;
            left: 0;
            margin-top: {spacing._2};
        }}

        .menu-bottom-right {{
            top: 100%;
            right: 0;
            margin-top: {spacing._2};
        }}

        .menu-top-left {{
            bottom: 100%;
            left: 0;
            margin-bottom: {spacing._2};
        }}

        .menu-top-right {{
            bottom: 100%;
            right: 0;
            margin-bottom: {spacing._2};
        }}

        .menu-item {{
            display: block;
            padding: {spacing._2} {spacing._4};
            color: {colors.text_primary};
            text-decoration: none;
            cursor: pointer;
            transition: background-color {transitions.fast};
        }}

        .menu-item:hover:not(.menu-item-disabled) {{
            background-color: {colors.background_alt};
        }}

        .menu-item-disabled {{
            pointer-events: none;
            opacity: 0.5;
        }}

        .menu-divider {{
            margin: {spacing._2} 0;
            border: none;
            border-top: {borders.default} solid {colors.border};
        }}

        /* Details/Summary dropdown menu support */
        .menu-wrapper {{
            position: relative;
            display: inline-block;
        }}

        .menu-wrapper > summary {{
            list-style: none;
            cursor: pointer;
        }}

        .menu-wrapper > summary::-webkit-details-marker {{
            display: none;
        }}

        .menu-wrapper > summary::marker {{
            display: none;
            content: "";
        }}

        .menu-wrapper[open] > .menu {{
            display: block;
        }}

        .menu-wrapper:not([open]) > .menu {{
            display: none;
        }}
        """


def _interactive_component_styles() -> str:
    """Generate interactive component styles."""
    return f"""
        /* ===== INTERACTIVE COMPONENTS ===== */

        /* Accordion */
        .accordion {{
            border: {borders.default} solid {colors.border};
            border-radius: {radius.md};
            overflow: hidden;
        }}

        .accordion-item {{
            border-bottom: {borders.default} solid {colors.border};
        }}

        .accordion-item:last-child {{
            border-bottom: none;
        }}

        .accordion-trigger {{
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: {spacing._4};
            background-color: transparent;
            border: none;
            cursor: pointer;
            font-size: {typography.base.size};
            font-weight: {typography.font_semibold};
            color: {colors.text_primary};
            transition: background-color {transitions.fast};
            text-align: left;
        }}

        .accordion-trigger:hover {{
            background-color: {colors.background_alt};
        }}

        .accordion-content {{
            padding: 0 {spacing._4} {spacing._4};
            color: {colors.text_secondary};
        }}

        /* Collapsible */
        .collapsible {{
            border: {borders.default} solid {colors.border};
            border-radius: {radius.md};
        }}

        /* Hide default summary marker for collapsible */
        .collapsible > summary {{
            list-style: none;
        }}

        .collapsible > summary::-webkit-details-marker {{
            display: none;
        }}

        .collapsible > summary::marker {{
            display: none;
            content: "";
        }}

        .collapsible-trigger {{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: {spacing._3};
            background-color: transparent;
            border: none;
            cursor: pointer;
            font-size: {typography.base.size};
            font-weight: {typography.font_medium};
            color: {colors.text_primary};
            transition: background-color {transitions.fast};
            text-align: left;
        }}

        .collapsible-trigger:hover {{
            background-color: {colors.background_alt};
        }}

        /* Rotate icon when collapsible is open */
        .collapsible[open] .collapsible-icon {{
            transform: rotate(180deg);
        }}

        .collapsible-content {{
            padding: {spacing._3};
            border-top: {borders.default} solid {colors.border};
        }}

        /* Pagination */
        .pagination {{
            display: flex;
            align-items: center;
            gap: {spacing._2};
        }}

        .pagination-item {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 2.5rem;
            height: 2.5rem;
            padding: {spacing._2};
            font-size: {typography.sm.size};
            color: {colors.text_primary};
            background-color: {colors.background};
            border: {borders.default} solid {colors.border};
            border-radius: {radius.md};
            cursor: default;
        }}

        .pagination-link {{
            cursor: pointer;
            text-decoration: none;
            transition: background-color {transitions.fast};
        }}

        .pagination-link:hover {{
            background-color: {colors.background_alt};
        }}

        .pagination-item-active {{
            background-color: {colors.primary.s600};
            color: white;
            border-color: {colors.primary.s600};
        }}

        .pagination-item-disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}

        .pagination-ellipsis {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 2.5rem;
            height: 2.5rem;
            color: {colors.text_secondary};
        }}

        /* Icon & Logo */
        .icon {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}

        .logo {{
            display: inline-flex;
            align-items: center;
        }}

        /* ===== ACCESSIBILITY ===== */

        .sr-only {{
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border-width: 0;
        }}

        /* Focus visible for keyboard navigation */
        *:focus-visible {{
            outline: 2px solid {colors.border_focus};
            outline-offset: 2px;
        }}
        """


def component_styles() -> str:
    """
    Generate component-specific CSS styles.

    Returns:
        CSS string with component styles
    """
    return (
        _layout_component_styles()
        + _button_component_styles()
        + _input_component_styles()
        + _feedback_component_styles()
        + _card_table_component_styles()
        + _modal_overlay_component_styles()
        + _tabs_accordion_component_styles()
        + _htmx_search_component_styles()
        + _enhanced_item_details_styles()
        + _responsive_page_specific_styles()
        + _overlay_component_styles()
        + _interactive_component_styles()
    )
