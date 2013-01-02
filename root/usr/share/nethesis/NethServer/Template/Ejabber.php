<?php

echo $view->header()->setAttribute('template', $T('Ejabber_Title'));

echo $view->panel()
    ->insert($view->checkbox('status', 'enabled')->setAttribute('uncheckedValue', 'disabled'));

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
?>
