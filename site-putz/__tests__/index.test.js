import React from "react";
import { render, screen } from '@testing-library/react';
import Home from '../pages/index';

describe('Home page', () => {
  it('renders the component text', () => {
    render(<Home />);
    expect(screen.getByText('Site PUTZ')).toBeInTheDocument();
  });
});
